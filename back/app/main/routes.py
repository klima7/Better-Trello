from . import main
from .. import auth
from flask import request, jsonify, abort
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


@main.route('/boards', methods=['POST'])
@auth.login_required
def add_board():
    user = auth.current_user()
    # Verify arguments
    if user is None:
        return abort(400, 'Login required')
    if 'name' not in request.json:
        return abort(400, 'Table\'s name was not found')
    name = request.json['name']
    if len(name) < 1:
        return abort(400, 'Table\'s name can not be blank')
    if len(name) > 40:
        return abort(400, 'Table\'s name can not exceed 40 characters')
    # Add new board db
    board = Board(name=name, user_id=user.id)
    db.session.add(board)
    db.session.commit()
    return {}, 200
