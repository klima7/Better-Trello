from flask import Blueprint

main = Blueprint('main', __name__)

from . import boards
from . import columns
from . import cards


@main.route('/')
def index():
    return 'Ok'
