from flask.globals import request
import requests
from flask import (Flask, jsonify, redirect, url_for, abort)
import json
import logging

app = Flask(__name__)

s = requests.Session()

def GETgreg():
	return None

def POSTgreg(data):
	return None

def Fetch():
	return None

@app.route("/api")
def index():
	return abort(418)

@app.route("/api/<key>/<method>")
def api(key, method):
	if method == "POST":
		POSTgreg(request.args.get("data"))
		return "POST"
	elif method == "GET":
		GETgreg()
		return "GET"
	else:
		return key
		#abort(410)

app.run()	