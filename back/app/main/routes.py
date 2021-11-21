from . import main
from .. import auth
from flask import json, request, jsonify, abort
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
        return abort(400, '\'name\' field was not found in request')
    name = request.json['name']
    if len(name) < 1:
        return abort(400, 'Board\'s name can not be blank')
    if len(name) > 40:
        return abort(400, 'Board\'s name can not exceed 40 characters')
    # Add new board db
    board = Board(name=name, user_id=user.id)
    db.session.add(board)
    db.session.commit()
    return {}, 200


@main.route('/info', methods=['POST'])
@auth.login_required
def get_board_info():
    user = auth.current_user()
    # Verify arguments
    if user is None:
        return abort(400, 'Login required')
    if 'id' not in request.json:
        return abort(400, '\'id\' field was not found in request')
    # Get board
    board_id = request.json['id']
    board_json = Board.query.filter_by(user_id=user.id, id=board_id).first().toJSON()
    if board_json is None:
        return abort(400, 'Board was not found')

    # Output dict
    columns_dict = []
    columns = Column.query.filter_by(board_id=board_id).all()
    for column in columns:
        cards = Card.query.filter_by(column_id=column.id).all()
        all_cards = []
        for card in cards:
            all_cards.append(card.toJSON())
        columns_dict.append({'name': column.name, 'cards': all_cards})
    if columns_dict is None:
        return {}, 200
    output_dict = {'board_name': board_json['name'], 'columns': columns_dict}
    return jsonify(output_dict), 200