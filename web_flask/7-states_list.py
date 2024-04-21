#!/usr/bin/python3
"""script that starts a Flask web application: listening on 0.0.0.0, port 5000
fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states_list")
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    Flask.run(app)
