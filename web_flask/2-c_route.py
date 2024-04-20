#!/usr/bin/env python3
''' Starts a Flask web app '''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Displays some text '''
    return "Hello HBNB!"

    
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Displays HBNB '''
    return "HBNB"

@app.route('/c/<text>')
def ctext(text):
    ''' Displays C followed by text '''
    if '_' in text:
        text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)