#!/usr/bin/env python3
""" Starts a Flask web app """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_bnb():
    return "Hello HBNB"