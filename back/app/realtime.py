from flask_socketio import emit


def notify_board_changed(board_id):
    emit('board-changed', {}, broadcast=True, namespace=f'/boardss/{board_id}')
