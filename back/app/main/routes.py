from . import main
from .. import auth
from flask import request, jsonify
from app.models import *

@main.route('/')
def index():
    return 'Ok'


@main.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    teacher = Todo(content=data['content'])
    db.session.add(teacher)
    db.session.commit()
    return 'Todo added'


@main.route('/todos', methods=['GET'])
@auth.login_required
def get_todos():
    todos = Todo.query.all()
    todos_json = [todo.to_json() for todo in todos]
    return jsonify(todos_json)

@main.route('/boards', methods=['GET'])
@auth.login_required
def get_board_list():
    user = auth.current_user()
    if user is not None:
        boards = Board.query.filter_by(user_id=user.id).all()
        return jsonify([
            {"id": b.id, "name": b.name} for b in boards
        ])
    return jsonify([])