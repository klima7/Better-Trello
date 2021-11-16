import jwt
from app import auth
from flask import current_app


@auth.verify_token
def verify_token(token):
    login, password = decode_token(token)
    if login is None or password is None:
        return None
    return login


def encode_token(login, password):
    return jwt.encode({'login': login, 'password': password}, current_app.config['SECRET_KEY'], algorithm='HS256')


def decode_token(token):
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        login = data.get('login')
        password = data.get('password')
        return login, password
    except:
        return None, None
