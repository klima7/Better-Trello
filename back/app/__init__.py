from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})
db = SQLAlchemy(app)

from app.models import *
db.create_all()

from app import routes

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth/')
