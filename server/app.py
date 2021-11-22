from flask import Flask, request, send_file, send_from_directory
from somef.cli import cli_get_data, run_cli

app = Flask(__name__)


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

    url = request.args.get('url')
    if url.find("https://github.com/") != 0:
        return "GitHub URL is not valid", 400

    metadata = cli_get_data(threshold, ignore_classifiers, repo_url=url)
    path = 'server/generated-files/metadata'
    run_cli(threshold=threshold, ignore_classifiers=ignore_classifiers, repo_url=url,
            output=path, graph_out=path, codemeta_out=path)
    if metadata is None:
        return "GitHub repository is not valid", 400
    else:
        return metadata


@app.route('/download')
def download_metadata():
    file_type = parse_file_type(request.args.get('fileType'))
    if file_type is None:
        return "Invalid file type for download", 400

    path = 'generated-files/'
    if file_type == 'json':
        try:
            return send_file(path+'metadata.json', as_attachment=True)
        except Exception:
            return "Metadata file not generated", 400

    elif file_type == 'codemeta':
        try:
            return send_file('metadata', as_attachment=True)
        except Exception:
            return "Metadata file not generated", 400


@app.route('/test')
def test():
    repo_url = 'https://github.com/KnowledgeCaptureAndDiscovery/somef'
    path = 'server/generated-files/'
    run_cli(threshold=0.8, ignore_classifiers=False, repo_url=repo_url,
            output=path+'metadata.json', graph_out=path+'metadata-turtle', codemeta_out=path+'metadata-codemeta')
    return send_file('generated-files/metadata.json', as_attachment=True)
    # return cli_get_data(0.8, False, repo_url=repo_url)


def parse_threshold(value):
    try:
        threshold = float(value)
        if 0 <= threshold <= 1:
            return threshold
    except ValueError:
        return None

    return None


def parse_ignore_classifiers(value):
    if value == 'true':
        return True
    elif value == 'false':
        return False
    else:
        return None


def parse_file_type(value):
    if value == 'json':
        return 'json'
    elif value == 'codemeta':
        return 'codemeta'
    elif value == 'turtle':
        return 'turtle'
    else:
        return None


if __name__ == '__main__':
    app.run()
