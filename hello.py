from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '왜 오류가 뜨는걸까 배포는 되는데 이상하네'


if __name__ == '__main__':
    app.run()