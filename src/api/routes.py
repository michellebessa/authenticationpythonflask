"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def sign_up():

    data = request.get_json()
    user = User(email = data["email"], password = data["password"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message":"user was created successfully"}), 200

@api.route('/login', methods=['POST'])
def login():

    data = request.get_json()
    if "email" not in data or data["email"] == "":
        return jsonify({"message":"email not found"})
    if "password" not in data or data["password"] == "":
        return jsonify({"message":"password not found"})

    user = User.query.filter_by(email=data["email"]).first()
    if user == None or data["password"] != user.password: 
        return jsonify({"message": "password is incorrect"})
    else: 
        access_token = create_access_token(identity=data["email"])
        return jsonify(access_token=access_token)