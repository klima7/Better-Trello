from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# association_table = db.Table('association',
#     db.Column('user', db.ForeignKey('User.id'), primary_key=True),
#     db.Column('board', db.ForeignKey('Board.id'), primary_key=True)
# )

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

    def toJSON(self):
        return {"id": self.id, "title": self.title, "description": self.description}


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

    shared_users = db.relationship("User", secondary='association', back_populates='shared_boards')

    def toJSON(self):
        return {"name": self.name}

    def userHasAccess(self, user_id):
        if user_id == self.user_id:
            return True
        b = Board.query.filter_by(id=self.id).filter(Board.shared_users.any(User.id == user_id)).first()
        return b != None
