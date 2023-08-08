#!/usr/bin/python3
""" dynamically list all states in the database using flask """

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_list():
    '''displays states and cities in alphabrtical order'''
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exceptiom):
    """closes storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
