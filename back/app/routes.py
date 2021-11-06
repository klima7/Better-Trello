from flask_cors import cross_origin

from app import app
from app.models import *
from flask import request
from flask import jsonify


@app.route('/')
def index():
    return 'Hello'


@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    teacher = Todo(content=data['content'])
    db.session.add(teacher)
    db.session.commit()
    return 'Todo added'


@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todos_json = [todo.to_json() for todo in todos]
    return jsonify(todos_json)
