from database.connection import execute_query
def update():
    heroes = """SELECT id, name FROM heroes"""
    heroes_result = execute_query(heroes).fetchall()
    for x in heroes_result:
        print("-"+str(x[1]))

    name = input("Who's about me do you want to update? ")
    new = input('Whats new about them? ')
    action = """UPDATE heroes
                SET about_me = %s
                WHERE name=%s"""
    execute_query(action,(new, name))