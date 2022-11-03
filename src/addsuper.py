from database.connection import execute_query
def create():
    name = input('Whats your super name? ')
    about = input('Tell me a little about yourself: ')
    bio = input('What is your backstory? ')
    action = """INSERT INTO heroes(name,about_me,biography) VALUES(%s,%s,%s)"""
    execute_query(action, (name, about, bio))