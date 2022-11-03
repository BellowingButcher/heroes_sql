from database.connection import execute_query;
def dispatch():
    heroes = """SELECT id, name FROM heroes"""
    heroes_result = execute_query(heroes).fetchall()
    for x in heroes_result:
        print("-"+str(x[1]))

    name = input('Who do you want to dispatch? ')
    action = """DELETE
                FROM heroes
                WHERE name = %s
                """
    execute_query(action, (name,))
