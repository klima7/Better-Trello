from . import main
from .. import auth
from flask import request, jsonify
from app.models import *


@main.route('/')
def index():
    return 'Ok'


@main.route('/todos', methods=['POST'])
def add_todo():
    print('add_todo', request.authorization, request.headers.get('Authorization'))
    data = request.json
    teacher = Todo(content=data['content'])
    db.session.add(teacher)
    db.session.commit()
    return 'Todo added'


@main.route('/todos', methods=['GET'])
@auth.login_required
def get_todos():
    print('Your are', auth.current_user())
    todos = Todo.query.all()
    todos_json = [todo.to_json() for todo in todos]
    return jsonify(todos_json)
