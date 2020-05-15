import sqlite3

# connect = sqlite3.connect('db.sqlite')
# cur = connect.cursor()

# query = """
# INSERT INTO phonebook (id, name, p_number) VALUES (0, 'Ярик', 88005553535);
# """

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

# query = "DROP TABLE groups"

query = "DELETE FROM groups WHERE id < 10"

# query = "INSERT INTO groups (group_name) VALUES ('User')"

# query = "SELECT * FROM groups"

# query = "SELECT * FROM answer;"

# query = f"INSERT INTO answer (msg, answ) VALUES ('фывафыав', 'ass');"
# cur.execute(query)
# create("aoao", "aoao")
# result = cur.fetchall()
# print(result)
# print(create('sadasf', 'asfasf'))

# print(create("ss", "sss"))

connect = sqlite3.connect('main_db.sqlite3')
cur = connect.cursor()

def insert_into(table, db_msg, db_answ):
    query = f"INSERT INTO {table} (msg, answ) VALUES ('{db_msg}', '{db_answ}');"
    cur.execute(query)
    return cur.fetchall()

def get(table, col="*"):
    query = f"SELECT {col} FROM {table}"
    cur.execute(query)
    return cur.fetchall()

# result = insert_into("answer", "привет", "Ну привет-привет, <name>")
# result = get("answer")
# print(result)

# query = "INSERT INTO answer (msg, answ) VALUES ('/teach', 'Бот выучил новую команду! level up 📈');"
query = "SELECT * FROM answer"

cur.execute(query)
result = cur.fetchall()
print(result)

connect.commit()
connect.close()


