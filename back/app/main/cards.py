from . import main
from .. import auth
from flask import request
from app.models import *


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

    card = Card(title=title, column_id=column_id, order=last_card_id + 1)
    db.session.add(card)
    db.session.commit()

    return card.toJSON(), 200


@main.route('/cards/<int:card_id>', methods=['PATCH'])
@auth.login_required
def card_patch(card_id):
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

    if request.json is None:
        return {}, 200

    if 'title' in request.json:
        title = request.json['title']
        if len(title) == 0 or len(title) > 4096:
            return 'Invalid title length', 400
        card.title = title

    if 'description' in request.json:
        description = request.json['description']
        if len(description) == 0 or len(description) > 4096:
            return 'Invalid description length', 400
        card.description = description

    if 'column' in request.json:
        response = _change_card_column(card, request.json['column'])
        if response: return response

    if 'order' in request.json:
        response = _change_card_order(card, request.json['order'])
        if response: return response

    db.session.commit()
    return {}, 200


def _change_card_column(card, new_column_id):
    current_column = Column.query.filter_by(id=card.column_id).first()
    new_column = Column.query.filter_by(id=new_column_id).first()

    if current_column.id == new_column.id:
        return None

    print('Changing column')

    if not current_column or not new_column:
        return 'Column not found', 404

    if current_column.board_id != new_column.board_id:
        return 'Unable to move columns between boards', 400

    _delete_card_from_column(card, current_column)
    _add_card_to_column(card, new_column)


def _delete_card_from_column(card_to_remove, column):
    cards = Card.query.filter_by(column_id=card_to_remove.column_id).all()
    cards = [card for card in cards if card.order > card_to_remove.order]
    for card in cards:
        card.order -= 1
    column.cards.remove(card_to_remove)


def _add_card_to_column(card_to_add, column):
    db.session.add(card_to_add)
    db.session.add(column)
    last_card = Card.query.filter_by(column_id=column.id).order_by(Card.order.desc()).first()
    next_card_order = last_card.order + 1 if last_card else 0
    card_to_add.order = next_card_order
    column.cards.append(card_to_add)


def _change_card_order(card, new_order):
    old_order = card.order
    if old_order == new_order:
        return

    order_min = min(old_order, new_order)
    order_max = max(old_order, new_order)

    cards = Card.query.filter_by(column_id=card.column_id).all()
    cards = [card for card in cards if order_min <= card.order <= order_max]

    for card in cards:
        if card.order == old_order:
            card.order = new_order
        elif new_order > old_order:  # moving right
            card.order -= 1
        else:  # moving left
            card.order += 1
