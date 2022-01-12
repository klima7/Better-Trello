from . import main
from .. import auth
from flask import request, jsonify
from app.models import *
import app.realtime as realtime


@main.route('/boards', methods=['GET'])
@auth.login_required
def get_board_list():
    user = auth.current_user()
    # boards = Board.query.filter_by(user_id=user.id).all()
    # shared_boards = Board.query.filter_by(user_id=user.id).all()

    print(user.shared_boards)

    return jsonify(
        {
            "owned_boards" : [{"id": b.id, "name": b.name, "shared_users": [u.email for u in b.shared_users]} for b in user.boards],
            "shared_boards": [{"id": b.id, "name": b.name} for b in user.shared_boards]
        }
    )


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
    board_json = Board.query.filter_by(id=board_id).first()
    if board_json is None or not board_json.userHasAccess(user.id):
        # board_json = Board.query.filter_by(id=board_id).filter(Board.shared_users.any(User.id == user.id)).first()
        # if board_json is None:
        return 'Board not found', 404
            
    board_json = board_json.toJSON()

    # Output
    columns_dict = []
    columns = Column.query.filter_by(board_id=board_id).order_by(Column.order.asc()).all()
    for column in columns:
        cards = Card.query.filter_by(column_id=column.id).order_by(Card.order.asc()).all()
        all_cards = []
        archived_cards = []
        for card in cards:
            if card.archived is False:
                all_cards.append(card.toJSON())
            else:
                archived_cards.append(card.toJSON())
        columns_dict.append({'name': column.name, 'id': column.id, 'board_id': board_id, 'cards': all_cards, 'archived_cards': archived_cards})
    if columns_dict is None:
        return {}, 200

    labels = Label.query.filter_by(board_id=board_id).order_by(Label.creation_time.asc()).all()
    labels_dict = [label.toJSON() for label in labels]

    output_dict = {'id': board_id, 'board_name': board_json['name'], 'columns': columns_dict, 'labels': labels_dict}
    print('labels', output_dict)


    return jsonify(output_dict), 200


@main.route('/boards/<int:board_id>', methods=['PATCH'])
@auth.login_required
def board_patch(board_id):
    user = auth.current_user()

    board = Board.query.filter_by(id=board_id).first()
    if board is None:
        return 'Board not found', 404

    if not board.userHasAccess(user.id):# board.user_id != user.id:
        return 'User is not owner of this board', 403

    if request.json and 'name' in request.json:
        name = request.json['name']
        if len(name) == 0 or len(name) > 30:
            return 'Invalid name length', 400
        board.name = name

    realtime.notify_board_changed(board_id)
    db.session.commit()
    return {}, 200

@main.route('/boards/<int:board_id>/share', methods=['POST'])
@auth.login_required
def share_board(board_id):
    user = auth.current_user()

    board = Board.query.filter_by(id=board_id).first()
    if board is None:
        return 'Board not found', 404

    if not board.userHasAccess(user.id):
        return 'User is not owner of this board', 403

    if request.json and 'email' in request.json:
        email = request.json['email']
        user_sharing = User.query.filter_by(email=email).first()
        if user_sharing and not board.userHasAccess(user_sharing.id):
            board.shared_users.append(user_sharing)
        # if len(name) == 0 or len(name) > 30:
        #     return 'Invalid name length', 400
        # board.name = name

            realtime.notify_user(user.id)
            for u in board.shared_users:
                realtime.notify_user(u.id)
            db.session.commit()
            return {}, 200

    return "Wrong username", 404


@main.route('/boards/<int:board_id>/sharestop', methods=['POST'])
@auth.login_required
def stop_sharing_board(board_id):
    user = auth.current_user()

    board = Board.query.filter_by(id=board_id).first()
    if board is None:
        return 'Board not found', 404

    if not board.userHasAccess(user.id):
        return 'User is not owner of this board', 403

    print("request json " + str(request.json))

    if request.json and 'email' in request.json:
        email = request.json['email']
        user_sharing = User.query.filter_by(email=email).first()
        if user_sharing and user_sharing in board.shared_users:
            board.shared_users.remove(user_sharing)

            realtime.notify_user(user.id)
            realtime.notify_user(user_sharing.id)
            for u in board.shared_users:
                realtime.notify_user(u.id)

            db.session.commit()
            return {}, 200

    return "Passed invalid user data", 404


@main.route('/boards/<int:board_id>/labels', methods=['POST'])
@auth.login_required
def add_label(board_id):
    user = auth.current_user()

    board = Board.query.filter_by(id=board_id).first()
    if board is None:
        return 'Board not found', 404

    if not board.userHasAccess(user.id):
        return 'User is not owner of this board', 403
    print(request.json)
    if not (request.json and 'text' in request.json and 'color' in request.json):
        return 'Missing data', 400

    text = request.json['text']
    color = request.json['color']

    label = Label(board_id=board_id, text=text, color=color)
    db.session.add(label)
    db.session.commit()

    realtime.notify_board_changed(board_id)

    return {}, 200
