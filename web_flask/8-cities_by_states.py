#!/usr/bin/python3

"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""

from models import storage
from flask import flask, render_template

@app.route("/cities_by_states", strict_slashes=False)
def citites_by_states():
     """Displays an HTML page with a list of all states and related cities.

     States/cities are sorted by name.
     """
     states = storage.all("State")
     return render_templates("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown():
    """Remove the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
