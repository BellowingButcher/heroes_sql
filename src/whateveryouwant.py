from database.connection import execute_query;

def execute_query("SELECT * FROM users", params=None):

SELECT heroes.id, relationships.relationship_type_id, relationship_type_id.name
FROM heroes
INNER JOIN relationships
ON heroes.id = relationships.hero1_id
INNER JOIN relationships
ON relationship_type_id.id = relationships.relationship_type_id