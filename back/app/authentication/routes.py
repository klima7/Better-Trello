from . import authentication
from .token import encode_token
from flask import jsonify, request, abort, Response
from app import db
from app.models import *


@authentication.route('/login', methods=['POST'])
def login():
    if 'login' not in request.json or 'password' not in request.json:
        return abort(400, 'Credentials not supplied')

    login = request.json['login']
    password = request.json['password']

    token = encode_token(login, password)

    resp = jsonify()
    resp.headers['Authorization'] = 'Bearer: ' + token
    return resp


@authentication.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']

    if len(password) < 8:
        return abort(400)

    exists = User.query.filter_by(email=email).first() is not None
    if exists:
        return abort(400)

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    token = encode_token(email, password)
    return jsonify({'token': token})


@authentication.route('/user', methods=['GET'])
def user():
    print('user ', request.headers.get('Authorization'))
    print('user ', request.authorization)
    return jsonify({'nick': 'klima7'})


@authentication.route('/refresh', methods=['GET'])
def refresh():
    return 'refresh'
