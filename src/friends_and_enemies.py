from database.connection import execute_query;
def friends_and_enemies_list():
    heroes = """SELECT id, name FROM heroes"""
    heroes_result = execute_query(heroes).fetchall()
    for x in heroes_result:
        print("-"+str(x[1]))
        
    name=input('Which heroes list do you want to see? The names are case sensitive: ')
    action = """SELECT
                    h1.name,
                    h2.name,
                    rt.name
                FROM relationships r
                    JOIN heroes h1 
                ON r.hero1_id = h1.id 
                    JOIN heroes h2
                ON r.hero2_id = h2.id
                    JOIN relationship_types rt
                ON r.relationship_type_id = rt.id
                    WHERE h1.name = %s"""
    result = execute_query(action, (name,)).fetchall()
    for x in result:
        print(x[1] + ' is a ' + x[2])