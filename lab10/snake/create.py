import psycopg2

connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    port=5432
)

create_table = '''
    CREATE TABLE IF NOT EXISTS snake(
        user_name  TEXT PRIMARY KEY NOT NULL,
        lvl INT,
        score INT, 
        points_snake TEXT
)
'''

cursor = connection.cursor()

try:
    cursor.execute('DROP TABLE IF EXISTS snake')
    cursor.execute(create_table)
    connection.commit()
    print('created!')
except Exception as error:
    print('ERROR:', error)
finally:
    connection.close()
