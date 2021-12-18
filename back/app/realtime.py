from flask_socketio import emit


def notify_board_changed(board_id):
    emit('board-changed', {}, broadcast=True, namespace=f'/boardss/{board_id}')

def notify_user(user_id):
    emit('users-board-changed', {}, broadcast=True, namespace=f'/usersz/{user_id}')