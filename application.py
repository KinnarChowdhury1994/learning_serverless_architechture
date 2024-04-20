from flask import Flask,request,jsonify
# from datetime import datetime
from utils import setup_logger

log = setup_logger('LOG', 'app.log')

#! Creating Server
app = Flask(__name__)

@app.route("/")
def hello():
    return "<H1>Flask Application is Running.</H1>"


if (__name__ == "__main__"):
    app.run(debug=True)