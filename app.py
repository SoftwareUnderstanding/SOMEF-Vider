from flask import Flask
from somef.cli import cli_get_data

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return cli_get_data(0.8, True, repo_url='https://github.com/dgarijo/Widoco/')


if __name__ == '__main__':
    app.run()
