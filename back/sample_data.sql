-- RESET DATABASE
    delete from user;
    delete from card;
    delete from column;
    delete from board;

-- SAMPLE USER
    insert into user(id, email, password_hash) values(1, 'test@test.com', 'pbkdf2:sha256:260000$7FipGbCSJh8EZyCp$3bc43811f2ce505071826fa8da1daf2c92d6685a928667aa1cf396651ee75368');

-- GROCERY LIST TEST BOARD
    -- CARDS
        insert into card(id, title, description, column_id) values(1, 'Herbs & Spices', 'Basil, Oregano, Coriander, Cumin', 1);
        insert into card(id, title, description, column_id) values(2, 'Breakfast cereal', 'Porridge oats, Unsweetened gransola', 2);
        insert into card(id, title, description, column_id) values(3, 'Oily fish', 'Tuna, Salmon, Mackerel', 2);
        insert into card(id, title, description, column_id) values(4, 'Pulses', 'Red kidney beans, White beans, Green lentils', 3);

    -- COLUMNS
        insert into column(id, name, board_id) values(1, 'To buy', 1);
        insert into column(id, name, board_id) values(2, 'In chart', 1);
        insert into column(id, name, board_id) values(3, 'Bought', 1);

    -- BOARDS
        insert into board(id, name, user_id) values (1, 'Standard Grocery List', 1);

-- WORKOUT ROUTINE TEST BOARD
    -- CARDS
        insert into card(id, title, description, column_id) values(5, 'Total body flow', 'Mat, resistance band', 4);
        insert into card(id, title, description, column_id) values(6, 'Cardio sculpt express', 'Mat, light hand weights', 4);
        insert into card(id, title, description, column_id) values(7, 'Ball workout', 'Mat and pilates/barre ball', 4);
        insert into card(id, title, description, column_id) values(8, 'Ballet glide & sculpt', 'Mat, chair, gliding disc (paper plates or rags)', 5);
        insert into card(id, title, description, column_id) values(9, 'Yoga fusion flow', 'Mat', 5);
        insert into card(id, title, description, column_id) values(10, 'Barre body blast', 'Mat, chair, light hand weights', 5);
        insert into card(id, title, description, column_id) values(11, 'Total body cardio sculpt', 'Mat, light hand weights', 5);
        insert into card(id, title, description, column_id) values(12, 'Upper + lower compound moves', 'Light hand weights', 6);
        insert into card(id, title, description, column_id) values(13, 'Total body mat workout', 'Mat', 6);
        insert into card(id, title, description, column_id) values(14, 'Quickfix total body workout', 'Mat', 6);
        insert into card(id, title, description, column_id) values(15, 'Quickfix ballet box', 'Light hand weights', 7);

    -- COLUMNS
        insert into column(id, name, board_id) values(4, 'New excercises', 2);
        insert into column(id, name, board_id) values(5, 'In current routine', 2);
        insert into column(id, name, board_id) values(6, 'Ideas for excercises', 2);
        insert into column(id, name, board_id) values(7, 'Past excercises', 2);

    -- BOARDS
        insert into board(id, name, user_id) values (2, 'Barlates Complete Workout Info List', 1);
