
import config

from flask import Flask, Response, request, current_app, jsonify, g
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    pass

@app.route("/register", methods=["POST"])
def register():
    pass

@app.route("/get-petition/<int:count>", methods=["POST"])
def get_petition(count):
    pass

#@login_required
@app.route("/change-my-pwd", methods=["POST"])
def change_my_pwd():
    pass

#@login_required
@app.route("/change-my-info", methods=["POST"])
def change_my_info():
    pass

#@login_required
@app.route("/write-petition", methods=["POST"])
def write_petition():
    pass

#@login_required
@app.route("/write-debate", methods=["POST"])
def write_debate():
    pass

#@login_required
@app.route("/support-petition", methods=["POST"])
def support_petition():
    pass