#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [START gae_python37_app]
import json

from flask import Flask, request
from flask_cors import CORS

from parser_util import get_terms, parse_strategy

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/search-parser", methods=['POST'])
def search_parser():
    query = request.get_data().decode("utf-8")
    response = app.response_class(
        response=json.dumps(parse_strategy(query)),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/search-parser/terms", methods=['POST'])
def search_terms():
    query = request.get_data().decode("utf-8")
    response = app.response_class(
        response=json.dumps(get_terms(query)),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
