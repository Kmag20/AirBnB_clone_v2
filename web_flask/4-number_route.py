#!/usr/bin/python3
""" Starts a Flask web app """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Displays some text '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Displays HBNB '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    ''' Displays C followed by text '''
    if '_' in text:
        text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    ''' Displays text in /python path '''
    if '_' in text:
        text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>')
def number(n):
    ''' Displays <n> is a number '''
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
