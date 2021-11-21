from app.models import *
from app import db

def add_sample_data():
    # RESET DATABASE
    User.query.delete()
    Card.query.delete()
    Column.query.delete()
    Board.query.delete()

    # SAMPLE USER (password: testtest)
    db.session.add(User(id=1, email='test@test.com', password_hash='pbkdf2:sha256:260000$7FipGbCSJh8EZyCp$3bc43811f2ce505071826fa8da1daf2c92d6685a928667aa1cf396651ee75368'))

    # GROCERY LIST TEST BOARD
    # CARDS
    db.session.add(Card(id=1, title='Herbs & Spices', description='Basil, Oregano, Coriander, Cumin', column_id=1))
    db.session.add(Card(id=2, title='Breakfast cereal', description='Porridge oats, Unsweetened gransola', column_id=2))
    db.session.add(Card(id=3, title='Oily fish', description='Tuna, Salmon, Mackerel', column_id=2))
    db.session.add(Card(id=4, title='Pulses', description='Red kidney beans, White beans, Green lentils', column_id=3))
    # COLUMNS
    db.session.add(Column(id=1, name='To buy', board_id=1))
    db.session.add(Column(id=2, name='In chart', board_id=1))
    db.session.add(Column(id=3, name='Bought', board_id=1))
    # BOARDS
    db.session.add(Board(id=1, name='Standard Grocery List', user_id=1))

    # WORKOUT ROUTINE TEST BOARD
    # CARDS
    db.session.add(Card(id=5, title='Total body flow', description='Mat, resistance band', column_id=4))
    db.session.add(Card(id=6, title='Cardio sculpt express', description='Mat, light hand weights', column_id=4))
    db.session.add(Card(id=7, title='Ball workout', description='Mat and pilates/barre ball', column_id=4))
    db.session.add(Card(id=8, title='Ballet glide & sculpt', description='Mat, chair, gliding disc (paper plates or rags)', column_id=5))
    db.session.add(Card(id=9, title='Yoga fusion flow', description='Mat', column_id=5))
    db.session.add(Card(id=10, title='Barre body blast', description='Mat, chair, light hand weights', column_id=5))
    db.session.add(Card(id=11, title='Total body cardio sculpt', description='Mat, light hand weights', column_id=5))
    db.session.add(Card(id=12, title='Upper + lower compound moves', description='Light hand weights', column_id=6))
    db.session.add(Card(id=13, title='Total body mat workout', description='Mat', column_id=6))
    db.session.add(Card(id=14, title='Quickfix total body workout', description='Mat', column_id=6))
    db.session.add(Card(id=15, title='Quickfix ballet box', description='Light hand weights', column_id=7))
    # COLUMNS
    db.session.add(Column(id=4, name='New excercises', board_id=2))
    db.session.add(Column(id=5, name='In current routine', board_id=2))
    db.session.add(Column(id=6, name='Ideas for excercises', board_id=2))
    db.session.add(Column(id=7, name='Past excercises', board_id=2))
    # BOARDS
    db.session.add(Board(id=2, name='Barlates Complete Workout List', user_id=1))
    db.session.commit()