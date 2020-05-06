import json
import os
import logging

from flask import Flask, jsonify
from flask_cors import CORS

# Env variables
ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS', '["*"]')
APP_VERSION = os.environ.get('APP_VERSION', '0.0.1')
FLASK_HOST = os.environ.get("FLASK_HOST", 'localhost')
FLASK_PORT = os.environ.get("FLASK_PORT", '9001')

# HTTP Codes
HTTP_SUCCESS = 200
HTTP_BAD_REQUEST = 400

# Init flask app
app = Flask(__name__)
CORS(app, origins=json.loads(ALLOWED_ORIGINS))
logging.info('CORS allowed origins set to ["*"]')

@app.route('/')
def welcome():
    """ Welcome Page. """
    return "Hello World. Never do Live Demos"

@app.route('/health')
def health_check():
    """ Health Check for Application. """
    return jsonify(health='up', app_version=APP_VERSION, reason='all good')


@app.route('/fibonacci/<places>', methods=['GET'])
def get_fibonacci(places=0):
    """ Gets list of fibonacci numbers up to number of places given. """
    try:
        places = int(places)
    except ValueError:
        return jsonify(error="parameter needs to be a positive integer."), HTTP_BAD_REQUEST

    fib_nums = [0, 1]
    if places < 0:
        return jsonify(error="parameter needs to be a positive integer."), HTTP_BAD_REQUEST
    if places == 0:
        return jsonify(results=list()), HTTP_SUCCESS
    if places < 2:
        return jsonify(results=fib_nums[:places]), HTTP_SUCCESS
    while places != len(fib_nums):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return jsonify(results=fib_nums), HTTP_SUCCESS


# This is not called when using gunicorn as wsgi
if __name__ == '__main__':
    logging.info('>>>>> Starting flask server at localhost:8080')
    app.run(host=FLASK_HOST, port=FLASK_PORT)
