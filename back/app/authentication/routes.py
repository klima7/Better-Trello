from . import authentication
from .token import encode_token
from flask import jsonify, request, abort


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
    print('register', request.json)
    resp = jsonify()
    return resp


@authentication.route('/user', methods=['GET'])
def user():
    print('user ', request.headers.get('Authorization'))
    print('user ', request.authorization)
    return jsonify({'nick': 'klima7'})


@authentication.route('/refresh', methods=['GET'])
def refresh():
    return 'refresh'
