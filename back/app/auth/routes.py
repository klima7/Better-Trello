from . import auth
from flask import jsonify, request, abort


@auth.route('/login', methods=['POST'])
def login():
    print('auth', request.authorization)
    username = request.authorization.username
    password = request.authorization.password
    if password != 'password':
        return abort(400, 'Invalid credentials')
    resp = jsonify()
    resp.headers['Authorization'] = request.headers.get('Authorization')
    return resp


@auth.route('/register', methods=['POST'])
def register():
    print('register', request.json)
    resp = jsonify()
    return resp


@auth.route('/user', methods=['GET'])
def user():
    print('user ', request.headers.get('Authorization'))
    print('user ', request.authorization)
    return jsonify({'nick': 'klima7'})


@auth.route('/refresh', methods=['GET'])
def refresh():
    return 'refresh'
