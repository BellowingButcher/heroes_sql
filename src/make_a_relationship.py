from database.connection import execute_query;
def make_a_relation():
        heroes = """SELECT id, name FROM heroes"""
        heroes_result = execute_query(heroes).fetchall()
        for x in heroes_result:
            print(str(x[0]) + '-' + str(x[1]))

        hero1_id=input('Choose the number beside who is starting the relationship? ')
        hero2_id=input('Choose the number beside who are they making this relationship with? ')
        relationship_type_id=input('Is this a 1-friend or a 2-enemy? Choose the number beside ')
        
        action = """INSERT INTO relationships(
                    hero1_id,
                    hero2_id,
                    relationship_type_id
                    )
                    VALUES(%s, %s, %s)
                    """

        execute_query(action,(hero1_id, hero2_id, relationship_type_id,))
