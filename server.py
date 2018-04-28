#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    query = request.get_data()
    response = app.response_class(
        response=json.dumps(parse_strategy(query)),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/search-parser/terms", methods=['POST'])
def search_terms():
    query = request.get_data()
    response = app.response_class(
        response=json.dumps(get_terms(query)),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(port=5002, host="0.0.0.0", threaded=True)
