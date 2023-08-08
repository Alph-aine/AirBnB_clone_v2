#!/usr/bin/python3
""" dynamically list all states in the database using flask """

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """displays states and cities in Alphabetical order"""
    states = storage.all('State')
    if state_id is not None:
        state_id = 'State.' + state_id
        render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exceptiom):
    """closes storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
