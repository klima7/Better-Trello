from . import authentication
from .. import auth
from .token import encode_token
from flask import jsonify, request, abort
from app.models import *


@authentication.route('/login', methods=['POST'])
def login():
    if 'email' not in request.json or 'password' not in request.json:
        return abort(400, 'Credentials not supplied')

    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()
    if not user.verify_password(password):
        abort(400, 'Invalid password')

    token = encode_token(email, password)

    resp = jsonify()
    resp.headers['Authorization'] = 'Bearer: ' + token
    return resp


@authentication.route('/register', methods=['POST'])
def register():
    if 'email' not in request.json or 'password' not in request.json:
        return abort(400, 'Credentials not supplied')

    email = request.json['email']
    password = request.json['password']

    if len(password) < 8:
        return abort(400, 'Password is too short')

    exists = User.query.filter_by(email=email).first() is not None
    if exists:
        return abort(400, 'User with this email already exists')

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return {}, 200


@authentication.route('/user', methods=['GET'])
@auth.login_required
def user():
    print('user: ', auth.current_user())
    return jsonify({'nick': 'klima7'})
