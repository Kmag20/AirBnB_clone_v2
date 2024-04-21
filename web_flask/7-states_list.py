#!/usr/bin/python3
''' Starts a flask web app '''

from flask import Flask, render_template
import sys
import os
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PARENT_DIR)

from models import storage




app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    ''' Remove current SQLAlchemy session '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' displays some HTML text '''
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
