from database.connection import execute_query;

def learn_about_who():
    heroes = """SELECT id, name FROM heroes"""
    heroes_result = execute_query(heroes).fetchall()
    for x in heroes_result:
        print(str(x[0]) + '-' + str(x[1]))
    name = input('Choose the number beside the hero are you inquiring about? ')
    action = """SELECT *
                FROM heroes WHERE id = %s"""

    result = execute_query(action, (name,)).fetchall()
    print('Hello my name is ' + result[0][1] + ' and ' + result[0][2])
    print('My story? Sure Ill tell you my story. Listen up!')
    print(result[0][3])
