from . import main
from .. import auth
from flask import request, jsonify
from app.models import *


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
    columns = Column.query.filter_by(board_id=board_id).order_by(Column.order.asc()).all()
    for column in columns:
        cards = Card.query.filter_by(column_id=column.id).order_by(Card.order.asc()).all()
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
def board_patch(board_id):
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
