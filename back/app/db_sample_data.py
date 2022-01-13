from app.models import *
from app import db


def add_sample_data():
    # RESET DATABASE
    User.query.delete()
    Card.query.delete()
    Column.query.delete()
    Board.query.delete()

    # GROCERY LIST TEST BOARD
    card1 = Card(order=0, title='Herbs & Spices', description='Basil, Oregano, Coriander, Cumin')
    card2 = Card(order=0, title='Breakfast cereal', description='Porridge oats, Unsweetened gransola')
    card3 = Card(order=1, title='Oily fish', description='Tuna, Salmon, Mackerel')
    card4 = Card(order=0, title='Pulses', description='Red kidney beans, White beans, Green lentils')

    col1 = Column(order=0, name='To buy', cards=[card1])
    col2 = Column(order=1, name='In chart', cards=[card2, card3])
    col3 = Column(order=2, name='Bought', cards=[card4])

    board1 = Board(name='Standard Grocery List', columns=[col1, col2, col3])

    label1 = Label(board=board1, text='Important', color='blue')


    # WORKOUT ROUTINE TEST BOARD
    card5 = Card(order=0, title='Total body flow', description='Mat, resistance band')
    card6 = Card(order=1, title='Cardio sculpt express', description='Mat, light hand weights')
    card7 = Card(order=2, title='Ball workout', description='Mat and pilates/barre ball')
    card8 = Card(order=0, title='Ballet glide & sculpt', description='Mat, chair, gliding disc (paper plates or rags)')
    card9 = Card(order=1, title='Yoga fusion flow', description='Mat')
    card10 = Card(order=2, title='Barre body blast', description='Mat, chair, light hand weights')
    card11 = Card(order=3, title='Total body cardio sculpt', description='Mat, light hand weights')
    card12 = Card(order=0, title='Upper + lower compound moves', description='Light hand weights')
    card13 = Card(order=1, title='Total body mat workout', description='Mat')
    card14 = Card(order=2, title='Quickfix total body workout', description='Mat')
    card15 = Card(order=0, title='Quickfix ballet box', description='Light hand weights')

    col4 = Column(order=0, name='New excercises', cards=[card5, card6, card7])
    col5 = Column(order=1, name='In current routine', cards=[card8, card9, card10, card11])
    col6 = Column(order=2, name='Ideas for excercises', cards=[card12, card13, card14])
    col7 = Column(order=3, name='Past excercises', cards=[card15])

    board2 = Board(name='Barlates Complete Workout List', columns=[col4, col5, col6, col7])

    card16 = Card(order=0, title='card', description='Tube snake boogie')
    col8 = Column(order=3, name='column', cards=[card16])
    board3 = Board(name='b3', columns=[col8])

    user = User(email='test@test.com', password="testtest", boards=[board1, board2], shared_boards=[board3])
    user2 = User(email='zz@top.com', password="zztop", boards=[board3], shared_boards=[board1, board2])
    user3 = User(email='vue@js.com', password="vuejs")

    # user.comments.append(comment1)

    # user2.shared_boards.append(board1)
    # user2.shared_boards.append(board2)
    # board3.shared_users.append(user)

    # FINISH
    db.session.add(user)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    comment1 = Comment(user_id=user.id, card_id=card1.id, content="content1")
    card1.comments.append(comment1)
    db.session.add(comment1)
    db.session.commit()
