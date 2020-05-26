from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '나도 관둘거야 나도 관둘거야 나도 관둘거야 나도 관둘거야 나도 관둘거야'


if __name__ == '__main__':
    app.run()