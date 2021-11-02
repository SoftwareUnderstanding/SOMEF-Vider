from flask import Flask, request
from somef.cli import cli_get_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/metadata')
def get_metadata():
    url = request.args.get('url')
    threshold = request.args.get('threshold')
    ignore_classifiers = request.args.get('ignoreClassifiers')

    return cli_get_data(threshold, ignore_classifiers, repo_url=url)


@app.route('/test')
def test():

    return cli_get_data(0.8, True, repo_url='https://github.com/KnowledgeCaptureAndDiscovery/somef')


if __name__ == '__main__':
    app.run()
