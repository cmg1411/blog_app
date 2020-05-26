from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'geolife is so hard ... i need something to rest...'


if __name__ == '__main__':
    app.run()