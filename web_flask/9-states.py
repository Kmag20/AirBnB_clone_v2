#!/usr/bin/python3
""" Starts a flask web application """
from flask import Flask
from flask import render_template
import sys
import os
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PARENT_DIR)
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
