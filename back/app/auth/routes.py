from . import auth
from flask import jsonify, request, abort, current_app
import jwt


@auth.route('/login', methods=['POST'])
def login():
    if 'login' not in request.json or 'password' not in request.json:
        return abort(400, 'Credentials not supplied')

    login = request.json['login']
    password = request.json['password']

    token = jwt.encode({'login': login, 'password': password}, current_app.config['SECRET_KEY'])

    resp = jsonify()
    resp.headers['Authorization'] = 'Bearer: ' + token
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
