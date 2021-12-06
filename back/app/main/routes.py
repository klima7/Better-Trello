from . import main
from .. import auth
from flask import json, request, jsonify
from app.models import *


@main.route('/')
def index():
    return 'Ok'


@main.route('/boards', methods=['GET'])
@auth.login_required
def get_board_list():
    user = auth.current_user()
    boards = Board.query.filter_by(user_id=user.id).all()
    return jsonify([
        {"id": b.id, "name": b.name} for b in boards
    ])


@main.route('/boards', methods=['POST'])
@auth.login_required
def add_board():
    user = auth.current_user()

    # Verify arguments
    if 'name' not in request.json:
        return 'name field was not found in request', 400
    name = request.json['name']
    if not 1 <= len(name) <= 40:
        return 'Invalid name length', 400

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
    if 'id' not in request.json:
        return 'Id field not found in request', 400

    # Get board
    board_id = request.json['id']
    board_json = Board.query.filter_by(user_id=user.id, id=board_id).first().toJSON()
    if board_json is None:
        return 'Board not found', 404

    # Output
    columns_dict = []
    columns = Column.query.filter_by(board_id=board_id).all()
    for column in columns:
        cards = Card.query.filter_by(column_id=column.id).all()
        all_cards = []
        for card in cards:
            all_cards.append(card.toJSON())
        columns_dict.append({'name': column.name, 'id': column.id, 'board_id': board_id, 'cards': all_cards})
    if columns_dict is None:
        return {}, 200
    output_dict = {'id': board_id, 'board_name': board_json['name'], 'columns': columns_dict}
    return jsonify(output_dict), 200


@main.route('/boards/<int:board_id>', methods=['PATCH'])
@auth.login_required
def board_update(board_id):
    user = auth.current_user()

    board = Board.query.filter_by(id=board_id).first()
    if board is None:
        return 'Board not found', 404

    if board.user_id != user.id:
        return 'User is not owner of this board', 403

    if request.json and 'name' in request.json:
        name = request.json['name']
        if len(name) == 0 or len(name) > 30:
            return 'Invalid name length', 400
        board.name = name

    db.session.commit()
    return {}, 200


@main.route('/cards/<int:card_id>', methods=['PATCH'])
@auth.login_required
def card_update(card_id):
    user = auth.current_user()

    card = Card.query.filter_by(id=card_id).first()
    if card is None:
        return 'Card not found', 404

    column = Column.query.filter_by(id=card.column_id).first()
    if column is None:
        return 'Column for card not found', 404

    board = Board.query.filter_by(id=column.board_id).first()
    if board is None:
        return 'Board for column not found', 404
    
    if board.user_id != user.id:
        return 'User is not owner of this board', 403

    if request.json and 'title' in request.json:
        title = request.json['title']
        if len(title) == 0 or len(title) > 4096:
            return 'Invalid title length', 400
        card.title = title

    if request.json and 'description' in request.json:
        description = request.json['description']
        if len(description) == 0 or len(description) > 4096:
            return 'Invalid description length', 400
        card.description = description

    db.session.commit()
    return {}, 200

@main.route('/boards/<int:board_id>/columns/<int:column_id>/cards', methods=['POST'])
@auth.login_required
def card_add(board_id, column_id):
    user = auth.current_user()

    if 'title' not in request.json:
        return 'Title not provided', 400
    title = request.json['title']

    if not 1 <= len(title) <= 30:
        return 'Invalid title length', 400

    board = Board.query.filter_by(id=board_id).first()
    if board is None:
        return 'Board not found', 404

    if board.user_id != user.id:
        return 'User is not owner of this board', 403

    column = Column.query.filter_by(id=column_id).first()
    if column is None:
        return 'Column not found in board', 404
    
    if column.board_id != board_id:
        return 'Column does not belong to this board', 403
    

    last_card = Card.query.filter_by(column_id=column_id).order_by(Card.order.desc()).first()
    last_card_id = last_card.order if last_card else 0

    card = Card(title=title, column_id=column_id, order=last_card_id+1)
    db.session.add(card)
    db.session.commit()

    return card.toJSON(), 200


@main.route('/boards/<int:board_id>/columns', methods=['POST'])
@auth.login_required
def column_add(board_id):
    user = auth.current_user()

    if 'name' not in request.json:
        return 'Name not provided', 400
    name = request.json['name']

    if not 1 <= len(name) <= 40:
        return 'Invalid name length', 400

    board = Board.query.filter_by(id=board_id).first()
    if board is None:
        return 'Board not found', 404

    if board.user_id != user.id:
        return 'User is not owner of this board', 403

    last_column = Column.query.filter_by(board_id=board_id).order_by(Column.order.desc()).first()
    last_column_id = last_column.order if last_column else 0

    column = Column(name=name, board_id=board_id, order=last_column_id+1)
    db.session.add(column)
    db.session.commit()

    return {}, 200
