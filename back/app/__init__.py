from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from config import Config

# Creating app
app = Flask(__name__)
app.config.from_object(Config)

# CORS setup
CORS(app)

# Extensions initialization
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPTokenAuth(scheme='Bearer')
socketio = SocketIO(app, cors_allowed_origins='*')

# Database initialization
from app.models import *
db.create_all()

from app.db_sample_data import add_sample_data

# Mounting blueprints
from .authentication import authentication as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth/')

from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/')


@app.cli.command('initdb', help='Initialize database with sample data')
def initdb():
    add_sample_data()
