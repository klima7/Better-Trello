from app import app
from app.models import *


@app.route('/')
def index():
    return 'Hello'


@app.route('/add/<content>')
def add(content):
    teacher = Todo(content=content)
    db.session.add(teacher)
    db.session.commit()
    return 'Added'
