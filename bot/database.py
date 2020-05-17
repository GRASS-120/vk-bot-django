import sqlite3

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

# query = "DROP TABLE answer"

def a():
    connect = sqlite3.connect('main_db.sqlite3')
    cur = connect.cursor()

    query = f"INSERT INTO groups (group_name) VALUES ('User');"
    
    cur.execute(query)
    cur.fetchall()

    connect.commit()
    connect.close()

def insert_into(table, msg, answ):
    connect = sqlite3.connect('main_db.sqlite3')
    cur = connect.cursor()

    query = f"INSERT INTO {table} (msg, answ) VALUES ('{msg}', '{answ}');"
    cur.execute(query)
    cur.fetchall()

    connect.commit()
    connect.close()

def get(table, col="*"):
    connect = sqlite3.connect('main_db.sqlite3')
    cur = connect.cursor()

    query = f"SELECT {col} FROM {table}"
    cur.execute(query)
    result = cur.fetchall()
    print(result)

    connect.commit()
    connect.close()
    return result


def delete(table):
    connect = sqlite3.connect('main_db.sqlite3')
    cur = connect.cursor()

    query = f"DELETE FROM {table}"
    cur.execute(query)
    cur.fetchall()

    connect.commit()
    connect.close()

def update(table, col, text, id):
    connect = sqlite3.connect('main_db.sqlite3')
    cur = connect.cursor()

    query_1 = f"UPDATE {table} SET {col} = '{text}' WHERE id = {id}"
    cur.execute(query_1)
    query_2 = f"SELECT {col} FROM {table} WHERE id = {id}"
    cur.execute(query_2)
    result = cur.fetchall()

    connect.commit()
    connect.close()
    return result

# a()
get("groups")







