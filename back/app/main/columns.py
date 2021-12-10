from . import main
from .. import auth
from flask import request
from app.models import *


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

    return column.toJSON(), 200


@main.route('/columns/<int:column_id>', methods=['PATCH'])
@auth.login_required
def column_patch(column_id):
    user = auth.current_user()

    column = Column.query.filter_by(id=column_id).first_or_404()

    if column.board.user != user:
        return 'User not permitted to edit column', 400

    if request.json is None:
        return {}, 200

    if 'order' in request.json:
        _move_column(column, request.json['order'])

    db.session.commit()
    return {}, 200


def _move_column(column, new_order):
    old_order = column.order
    if old_order == new_order:
        return

    order_min = min(old_order, new_order)
    order_max = max(old_order, new_order)

    columns = column.board.columns

    if new_order < 0 or new_order >= len(columns):
        return 'Invalid order provided'

    columns_to_modify = [column for column in columns if order_min <= column.order <= order_max]

    for column in columns_to_modify:
        if column.order == old_order:
            column.order = new_order
        elif new_order > old_order:     # moving right
            column.order -= 1
        else:   # moving left
            column.order += 1
