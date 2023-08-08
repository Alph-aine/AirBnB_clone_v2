#!/usr/bin/python3
""" dynamically list all states in the database using flask """

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """displays a  HTML page with the dynamic data"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    render_template('10-hbnb_filters.html', states=states,
                    amenities=amenities)


@app.teardown_appcontext
def teardown(exceptiom):
    """closes storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
