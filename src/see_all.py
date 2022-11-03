from database.connection import execute_query;

def see_all():
    heroes = """SELECT id, name FROM heroes"""
    heroes_result = execute_query(heroes).fetchall()
    for x in heroes_result:
        print('-' + str(x[1]))


