from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Creating app
app = Flask(__name__)
app.config.from_object(Config)

# CORS setup
CORS(app, resources={r'/*': {'origins': '*'}})

# Extensions initialization
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')

# Database initialization
from app.models import *
db.create_all()

# Mounting blueprints
from .authentication import authentication as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth/')

from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/')
