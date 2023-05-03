import json
import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')


@user.route('/register', methods=["POST"])
def register():
    payload = request.get_json()

    payload['email'] = payload['email'].lower()
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(data={}, status={"code": 401, "message": "A user with that email already exists."})
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.User.create(**payload)

        login_user(user)

        user_dict = model_to_dict(user)
        del user_dict['password']
        return jsonify(data=user_dict, status={'code': 201, 'message': 'Success'})


@user.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    try:
        user = models.User.get(models.User.email == payload['email'])
        user_dict = model_to_dict(user)
        if (check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            return jsonify(data=user_dict, status={'code': 200, 'message': 'user succesfully logged in'})
        else:
            return jsonify(data={}, status={'code': 401, 'message': 'Username or password does not match'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Username or password does not match'})
