#!/usr/bin/python3
"""a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)
"""The Flask application instance."""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    '''to run the Flask development server.'''
    app.run(host='0.0.0.0', port='5000')
