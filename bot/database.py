import sqlite3

connect = sqlite3.connect('db.sqlite')
cur = connect.cursor()

# query = """
# INSERT INTO phonebook (id, name, p_number) VALUES (0, 'Ярик', 88005553535);
# """

# query = "SELECT * FROM answer;"

def create(db_msg, db_answ):
    query = f"INSERT INTO answer (msg, answ) VALUES ('{db_msg}', '{db_answ}');"
    cur.execute(query)
    return cur.fetchall()

# query = """
# CREATE TABLE groups(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     group_name TEXT
# )
# """

# query = """
# CREATE TABLE users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     group_id INT,
#     FOREIGN KEY (group_id) REFERENCES groups(id)
# )
# """

# query = "INSERT INTO users (group_id) VALUES (1)"

cur.execute()
result = cur.fetchall()
# print(create('sadasf', 'asfasf'))

connect.commit()
connect.close()