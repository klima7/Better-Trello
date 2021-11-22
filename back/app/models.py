from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    boards = db.relationship("Board", backref="board", lazy='select')

    @property
    def password(self):
        raise AttributeError('Password is read only')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String)
    column_id = db.Column(db.Integer, db.ForeignKey('column.id'))

    def toJSON(self):
        return {"title": self.title, "description": self.description}


class Column(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    cards = db.relationship("Card", backref="card", lazy='select')
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))

    def toJSON(self):
        return {"name": self.name}


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    columns = db.relationship("Column", backref="column", lazy='select')

    def toJSON(self):
        return {"name": self.name}
