from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS
from somef.cli import cli_get_data, run_cli

app = Flask(__name__)
CORS(app)

dict_filename = {
    "json": "metadata.json",
    "codemeta": "codemeta.json",
    "turtle": "graph.ttl"
}


@app.route('/')
def index():
    return send_file('static/index.html')


@app.route('/js/<path:filename>')
def serve_static_js(filename):
    return send_from_directory('static/js', filename)


@app.route('/css/<path:filename>')
def serve_static_css(filename):
    return send_from_directory('static/css', filename)


@app.route('/metadata')
def get_metadata():
    threshold = parse_threshold(request.args.get('threshold'))
    if threshold is None:
        return "Threshold is not Valid", 400

    ignore_classifiers = parse_ignore_classifiers(request.args.get('ignoreClassifiers'))
    if ignore_classifiers is None:
        return "Ignore Classifiers flag is not a boolean", 400

    repo_url = request.args.get('url')
    if repo_url.find("https://github.com/") != 0:
        return "GitHub URL is not valid", 400

    path = 'server/generated-files/'

    try:
        run_cli(threshold=threshold, ignore_classifiers=ignore_classifiers, repo_url=repo_url,
                output=path+dict_filename.get("json"),
                codemeta_out=path+dict_filename.get("codemeta"),
                graph_out=path+dict_filename.get("turtle"))

        return send_from_directory('generated-files', dict_filename.get("json"))
    except Exception:
        return "Error extracting metadata from SOMEF", 400


@app.route('/download')
def download_metadata():
    filename = dict_filename.get(request.args.get('filetype'))
    if filename is None:
        return "Invalid file type for download", 400

    try:
        return send_from_directory('generated-files', filename, as_attachment=True)
    except Exception:
        return "Requested file not found", 400


@app.route('/test')
def test():
    repo_url = 'https://github.com/KnowledgeCaptureAndDiscovery/somef'

    return send_from_directory('generated-files', dict_filename.get("turtle"), as_attachment=True)


def parse_threshold(value):
    """Extract threshold value from the param for validation.
    :param value: Input threshold value.
    :return: A Float between 0 and 1, otherwise ``None``.
    """
    try:
        threshold = float(value)
        if 0 <= threshold <= 1:
            return threshold
    except ValueError:
        return None

    return None


def parse_ignore_classifiers(value):
    """Extract flag ignore classifiers value from the param for validation.
    :param value: Input ignore_classifiers value.
    :return: A Boolean value [True, False], otherwise ``None``.
    """
    if value == 'true':
        return True
    elif value == 'false':
        return False
    else:
        return None


if __name__ == '__main__':
    app.run()
