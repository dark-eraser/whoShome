from flask import request, jsonify
import flask
from Main import util

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# A route to return all of the available entries in our catalog.
@app.route('/', methods=['GET'])
def home():
    resp = jsonify(util())
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

app.run()