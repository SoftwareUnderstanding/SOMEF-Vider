import flask_cors
from flask import Flask
from somef.cli import cli_get_data
from flask_cors import CORS

app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/test')
def test():  # put application's code here

    return cli_get_data(0.8, True, repo_url='https://github.com/KnowledgeCaptureAndDiscovery/somef/')


if __name__ == '__main__':
    app.run()
