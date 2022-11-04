from database.connection import execute_query
def create():
    name = input('What is the super heroes name? ')
    about = input('A short about me for this hero: ')
    bio = input('A backstory for this hero ')
    action = """INSERT INTO heroes(name,about_me,biography) VALUES(%s,%s,%s)"""
    execute_query(action, (name, about, bio))