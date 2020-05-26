from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '관두지마 어딜 갈려그래 빨리 나어서 돌아와야지'


if __name__ == '__main__':
    app.run()