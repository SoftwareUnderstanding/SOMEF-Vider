from flask import Flask, request, render_template, send_file
from somef.cli import cli_get_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/metadata')
def get_metadata():
    threshold = request.args.get('threshold')
    if not validate_threshold(threshold):
        return "Threshold is not Valid", 400

    ignore_classifiers = request.args.get('ignoreClassifiers')
    if ignore_classifiers != 'True' \
            and ignore_classifiers != 'False'\
            and ignore_classifiers != '0'\
            and ignore_classifiers != '1':
        return "Ignore Classifiers flag is not a boolean", 400
    else:
        ignore_classifiers = bool(ignore_classifiers)

    url = request.args.get('url')
    if url.find("https://github.com/") != 0:
        return "GitHub URL is not valid", 400

    metadata = cli_get_data(threshold, ignore_classifiers, repo_url=url)
    if metadata is None:
        return "GitHub repository is not valid", 400
    else:
        return metadata, 200


@app.route('/test')
def test():
    return cli_get_data(0.8, False, repo_url='https://github.com/KnowledgeCaptureAndDiscovery/somef')


def validate_threshold(threshold):
    try:
        threshold = float(threshold)
        if threshold < 0 or threshold > 1:
            return False
    except ValueError:
        return False

    return True


if __name__ == '__main__':
    app.run()
