from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    def to_json(self):
        return {"content": self.content}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    boards = db.relationship("Board", backref="board", lazy='select')


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String)
    column_id = db.Column(db.Integer, db.ForeignKey('column.id'))


class Column(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cards = db.relationship("Card", backref="card", lazy='select')
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    columns = db.relationship("Column", backref="column", lazy='select')
