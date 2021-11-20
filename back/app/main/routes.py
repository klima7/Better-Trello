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

@app.route('/boards/<int:user_id>', methods=['GET'])
def get_board_list(user_id):
    boards = Board.query.filter_by(user_id=user_id).all()
    return jsonify([
        {"id": b.id, "name": b.name} for b in boards
    ])