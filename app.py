import os
from flask import Flask, render_template, request
from flask import make_response, jsonify, session

from flask.views import MethodView

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["TESTING"] = True

    book = {}
