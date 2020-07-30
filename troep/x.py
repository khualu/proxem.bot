from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return 'lol'


@app.route('/hallo/<path:name>')
def hoi(name):
    return 'hoi %s' % name


app.run(host='127.0.0.1', port=1337, debug=True)
