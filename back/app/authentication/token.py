import jwt
from app import auth
from flask import current_app
from app.models import User


@auth.verify_token
def verify_token(token):
    email, password = decode_token(token)
    if email is None or password is None:
        return None
    user = User.query.filter_by(email=email).first()
    if user is None or not user.verify_password(password):
        return None
    return user


def encode_token(email, password):
    return jwt.encode({'login': email, 'password': password}, current_app.config['SECRET_KEY'], algorithm='HS256')


def decode_token(token):
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        email = data.get('login')
        password = data.get('password')
        return email, password
    except:
        return None, None
