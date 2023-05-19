#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return "HBNB"

@app.route("/c/<string:text>", strict_slashes=False)
def c_text(text):
    """displays 'C' followed by the value of the text"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_text(text):
    """displays 'Python' followed by the value of the text"""
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
