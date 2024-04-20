#!/usr/bin/env python3
""" Starts a Flask web app """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_bnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', strict_slashes=False)