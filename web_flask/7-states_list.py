#!/usr/bin/python3
""" dynamically list all states in the database using flask """

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    '''gets the list of states from database in alphabetical order'''
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exceptiom):
    """closes storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
