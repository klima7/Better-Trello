from app.models import *
from app import db


def add_sample_data():
    # RESET DATABASE
    User.query.delete()
    Card.query.delete()
    Column.query.delete()
    Board.query.delete()

    # SAMPLE USER (password: testtest)
    db.session.add(User(id=1, email='test@test.com', password="testtest"))

    # GROCERY LIST TEST BOARD
    # CARDS
    db.session.add(Card(id=1, order=0, title='Herbs & Spices', description='Basil, Oregano, Coriander, Cumin', column_id=1))
    db.session.add(Card(id=2, order=0, title='Breakfast cereal', description='Porridge oats, Unsweetened gransola', column_id=2))
    db.session.add(Card(id=3, order=1, title='Oily fish', description='Tuna, Salmon, Mackerel', column_id=2))
    db.session.add(Card(id=4, order=2, title='Pulses', description='Red kidney beans, White beans, Green lentils', column_id=3))
    # COLUMNS
    db.session.add(Column(id=1, order=0, name='To buy', board_id=1))
    db.session.add(Column(id=2, order=1, name='In chart', board_id=1))
    db.session.add(Column(id=3, order=2, name='Bought', board_id=1))
    # BOARDS
    db.session.add(Board(id=1, name='Standard Grocery List', user_id=1))

    # WORKOUT ROUTINE TEST BOARD
    # CARDS
    db.session.add(Card(id=5, order=0, title='Total body flow', description='Mat, resistance band', column_id=4))
    db.session.add(Card(id=6, order=1, title='Cardio sculpt express', description='Mat, light hand weights', column_id=4))
    db.session.add(Card(id=7, order=2, title='Ball workout', description='Mat and pilates/barre ball', column_id=4))
    db.session.add(Card(id=8, order=0, title='Ballet glide & sculpt', description='Mat, chair, gliding disc (paper plates or rags)', column_id=5))
    db.session.add(Card(id=9, order=1, title='Yoga fusion flow', description='Mat', column_id=5))
    db.session.add(Card(id=10, order=2, title='Barre body blast', description='Mat, chair, light hand weights', column_id=5))
    db.session.add(Card(id=11, order=3, title='Total body cardio sculpt', description='Mat, light hand weights', column_id=5))
    db.session.add(Card(id=12, order=0, title='Upper + lower compound moves', description='Light hand weights', column_id=6))
    db.session.add(Card(id=13, order=1, title='Total body mat workout', description='Mat', column_id=6))
    db.session.add(Card(id=14, order=2, title='Quickfix total body workout', description='Mat', column_id=6))
    db.session.add(Card(id=15, order=0, title='Quickfix ballet box', description='Light hand weights', column_id=7))
    # COLUMNS
    db.session.add(Column(id=4, order=0, name='New excercises', board_id=2))
    db.session.add(Column(id=5, order=1, name='In current routine', board_id=2))
    db.session.add(Column(id=6, order=2, name='Ideas for excercises', board_id=2))
    db.session.add(Column(id=7, order=3, name='Past excercises', board_id=2))
    # BOARDS
    db.session.add(Board(id=2, name='Barlates Complete Workout List', user_id=1))
    db.session.commit()
