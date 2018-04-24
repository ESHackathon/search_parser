#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Flask, request

from parser_util import get_terms

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/search-parser", methods=['POST'])
def search_parser():
    query = request.get_data()
    return json.dumps(get_terms(query))

if __name__ == "__main__":
    app.run(port=5002, host="0.0.0.0", threaded=True)
