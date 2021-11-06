from app import app
from app.models import *
from flask import request


@app.route('/')
def index():
    return 'Hello'


@app.route('/todos', methods=['POST'])
def add():
    data = request.json
    teacher = Todo(content=data['content'])
    db.session.add(teacher)
    db.session.commit()
    return 'Todo added'
