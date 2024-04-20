#!/usr/bin/python3
"""
a script that starts a Flask web application:
The web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)
'''
Create an instance of the Flask class, which will
represent your web application:
'''


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''
    Logic to handle the request and generate a response
    that displays 'Hello HBNB!'
    '''
    return "Hello HBNB!"


if __name__ == "__main__":
    '''to run the Flask development server.'''
    app.run(host="0.0.0.0", port=5000)
