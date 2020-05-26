from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '잘 됬으면 좋겠다'


if __name__ == '__main__':
    app.run()