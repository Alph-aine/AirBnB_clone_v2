#!/usr/bin/python3
"""
  starts a flask web application
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns Hello  HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns Hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ returns C + text whilst removing all underscores in the text """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """ displays python + text, and replaces _ with space"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_int(n):
    """ display n onli if it is an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ returns a template with the value f n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_even(n):
    """checks if number is even or odd"""
    eveness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, eveness=eveness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
