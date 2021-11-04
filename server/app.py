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
    if metadata is None:
        return "GitHub repository is not valid", 400
    else:
        return metadata


@app.route('/test')
def test():
    return cli_get_data(0.8, False, repo_url='https://github.com/KnowledgeCaptureAndDiscovery/somef')


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


if __name__ == '__main__':
    app.run()
