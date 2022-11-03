# hero_table = execute_query(query)
name = input('What hero are you inquiring about? ')
action = """SELECT *
            FROM heroes WHERE name = %s"""

result = execute_query(action, (name,)).fetchall()
print('Hello my name is ' + result[0][1] + ' and ' + result[0][2])
print('My story? Sure Ill tell you my story. Listen up!')
print(result[0][3])