import flask_cors
from flask import Flask
from flask import request
from somef.cli import cli_get_data
from flask_cors import CORS

app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/metadata')
def get_metadata():
    url = request.args.get('url')
    threshold = request.args.get('threshold')
    ignore_classifiers = request.args.get('ignoreClassifiers')

    return cli_get_data(threshold, ignore_classifiers, repo_url=url)


if __name__ == '__main__':
    app.run()
