from database.connection import execute_query
def update():
    name = input('Whats your name? ')
    new = input('Whats new about you? ')
    action = """UPDATE heroes
                SET about_me = %s
                WHERE name=%s"""
    execute_query(action,(new, name))