"""
Flask dispatcher

This module provides the Flask dispatcher

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by Michael Batz, see AUTORS for more details
"""
import os
import flask

def app_init():
    """Flask app init"""
    basedir = os.path.dirname(os.path.abspath(__file__))
    flask_app = flask.Flask("yourCMDB2")
    flask_app.root_path = basedir
    #flask_app.secret_key = config.get_value("Webserver", "secret", "notsosecretkey")
    return flask_app
app = app_init()

@app.route("/")
def index():
    return "Hello World!"
