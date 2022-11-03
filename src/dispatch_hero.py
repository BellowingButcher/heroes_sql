from database.connection import execute_query;

name = input('Who do you want to dispatch? ')
action = """DELETE
            FROM heroes
            WHERE name = %s
            """
execute_query(action, (name,))
