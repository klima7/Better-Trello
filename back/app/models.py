from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()

class Association(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    board = db.Column(db.Integer, db.ForeignKey('board.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    boards = db.relationship("Board", backref="user", lazy='select')

    shared_boards = db.relationship("Board", secondary='association', back_populates='shared_users')
    comments = db.relationship("Comment", backref="user", lazy='select')

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
    order = db.Column(db.Integer)
    comments = db.relationship("Comment", backref="card", lazy="select")
    archived = db.Column(db.Boolean, default=False)
    labels = db.Column(db.PickleType, default=[])   # Python list of labels

    def toJSON(self):
        return {"id": self.id, "title": self.title, "description": self.description, "comments": [
            c.toJSON() for c in self.comments
        ]}

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    # user = db.relationship(User)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))

    def toJSON(self):
        user = User.query.filter_by(id=self.user_id).first()
        # board_json = Board.query.filter_by(id=board_id).first()
        return {"id": self.id, "content": self.content, "user": user.email}

class Column(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    cards = db.relationship("Card", backref="column", lazy='select')
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    order = db.Column(db.Integer)

    def toJSON(self):
        return {"id": self.id, "name": self.name}

    @property
    def last_card(self):
        return Card.query.filter_by(column_id=self.id).order_by(Card.order.desc()).first()

    @property
    def next_card_order(self):
        last_card = self.last_card
        return last_card.order+1 if last_card else 0

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    columns = db.relationship("Column", backref="board", lazy='select')
    labels = db.relationship("Label", backref="board", lazy='select')
    shared_users = db.relationship("User", secondary='association', back_populates='shared_boards')

    def toJSON(self):
        return {"name": self.name}

    def userHasAccess(self, user_id):
        if user_id == self.user_id:
            return True
        b = Board.query.filter_by(id=self.id).filter(Board.shared_users.any(User.id == user_id)).first()
        return b != None

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    creation_time = db.Column(db.DateTime, default=datetime.utcnow)
    text = db.Column(db.String(20))
    red = db.Column(db.Integer)
    green = db.Column(db.Integer)
    blue = db.Column(db.Integer)

    def toJSON(self):
        return {"id": self.id, "text": self.text, "red": self.red, "green": self.green, "blue": self.blue}