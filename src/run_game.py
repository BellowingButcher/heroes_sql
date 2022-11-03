from database.connection import execute_query;
from addsuper import create
from update_about_me import update
from dispatch_hero import dispatch
from friends_and_enemies import friends_and_enemies_list
from learn_about_who import learn_about_who

def run_game():
    choice = input('Thank you for accessing the Super Hero database.  Here you have the ability to create, update, or dispatch super heroes in our database. If you are wanting to create a super hero, please enter CREATE.  If you want to make changes to a super hero, please enter UPDATE.  If you are wanting to dispatch a hero, please enter DISPATCH.  You also have the option to view a table of friends and enemies. Enter READ for this list. To learn about a character type LEARN. If you are still confused, enter HELP. ' )
    choice = choice.upper()
    if choice == 'HELP':
        print('Type CREATE, UPDATE, DISPATCH, or READ to make a hero, update a hero, remove a hero, or read a list of friends and enemies for a hero')
        after_help()

    elif choice == 'CREATE':
        create()
        onward()
    elif choice == 'UPDATE':
        update()
        onward()
    elif choice == 'DISPATCH':
        dispatch()
        onward()
    elif choice == 'READ':
        friends_and_enemies_list()
        onward()
    elif choice == 'LEARN':
        learn_about_who()
        onward()
    else:
        print('I dont know what you want to do. Try HELP again')
        after_help()

def after_help():
    choice = input(' ')
    if choice == 'CREATE':
        create()
        onward()
    elif choice == 'UPDATE':
        update()
        onward()
    elif choice == 'DISPATCH':
        dispatch()
        onward()
    elif choice == 'READ':
        friends_and_enemies_list()
    elif choice == 'LEARN':
        learn_about_who()
        onward()
    else:
        print('I dont know what you want to do. Try HELP again')
        after_help()

def onward():
    choice = input('What do you want to do now? ')
    if choice == 'CREATE':
        create()
        onward()
    elif choice == 'UPDATE':
        update()
        onward()
    elif choice == 'DISPATCH':
        dispatch()
        onward()
    elif choice == 'READ':
        friends_and_enemies_list()
        onward()
    else:
        print('I dont know what you want to do. Try CREATE, UPDATE, DISPATCH, or READ')
        onward()

run_game()