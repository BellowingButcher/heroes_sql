from database.connection import execute_query;
from addsuper import create
from update_about_me import update
from dispatch_hero import dispatch
from friends_and_enemies import friends_and_enemies_list
from learn_about_who import learn_about_who
from make_a_relationship import make_a_relation
from see_all import see_all

def run_game():
    choice = input('Thank you for accessing the Super Hero database. Use one of the following keywords to interact with our database: CREATE, UPDATE, DISPATCH, RELATIONS, LEARN, CONNECTIONS, LIST, HELP: ').upper()
    if choice == 'HELP':
        print('CREATE - Add a new super hero to the database\nUPDATE - Change the about me of a specific hero\n DISPATCH - Remove hero from the database\nRELATIONS - Display a list of friends and enemies of an entered hero\nLEARN - Learn about a specific hero\nCONNECTIONS - Make a new friend, or enemy\nLIST - See a list of all the heroes in the database\nHELP - See this prompt')
        onward()

    elif choice == 'CREATE':
        create()
        onward()
    elif choice == 'UPDATE':
        update()
        onward()
    elif choice == 'DISPATCH':
        dispatch()
        onward()
    elif choice == 'RELATIONS':
        friends_and_enemies_list()
        onward()
    elif choice == 'LEARN':
        learn_about_who()
        onward()
    elif choice == 'CONNECTIONS':
        make_a_relation()
        onward()
    elif choice == 'LIST':
        see_all()
        onward()
    else:
        print("That wasn't a command")
        onward()

def onward():
    choice = input('What do you want to do now? ').upper()
    if choice == 'HELP':
        print('CREATE - Add a new super hero to the database\nUPDATE - Change the about me of a specific hero\n DISPATCH - Remove hero from the database\nRELATIONS - Display a list of friends and enemies of an entered hero\nLEARN - Learn about a specific hero\nCONNECTIONS - Make a new friend, or enemy\nLIST - See a list of all the heroes in the database\nHELP - See this prompt')
    if choice == 'CREATE':
        create()
        onward()
    elif choice == 'UPDATE':
        update()
        onward()
    elif choice == 'DISPATCH':
        dispatch()
        onward()
    elif choice == 'RELATIONS':
        friends_and_enemies_list()
        onward()
    elif choice == 'LEARN':
        learn_about_who()
        onward()
    elif choice == 'CONNECTIONS':
        make_a_relation()
        onward()
    elif choice == 'LIST':
        see_all()
        onward()
    else:
        print("That wasn't a command")
        onward()

run_game()