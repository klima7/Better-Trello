from flask import Blueprint

authentication = Blueprint('authentication', __name__)

from . import routes
from . import token
