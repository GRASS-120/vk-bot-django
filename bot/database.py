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

# query = "DELETE FROM groups WHERE id < 10"

# query = "SELECT * FROM answer;"

def insert_into(table, db_msg, db_answ):
    connect = sqlite3.connect('main_db.sqlite3')
    cur = connect.cursor()

    query = f"INSERT INTO {table} (msg, answ) VALUES ('{db_msg}', '{db_answ}');"
    cur.execute(query)
    cur.fetchall()

    connect.commit()
    connect.close()

def get(table, col="*"):
    connect = sqlite3.connect('main_db.sqlite3')
    cur = connect.cursor()

    query = f"SELECT {col} FROM {table}"
    cur.execute(query)
    print(cur.fetchall())

    connect.commit()
    connect.close()

get("answer")
# insert_into("answer", "/start", "Бот-вк начинает работу! 🤖\n Доступные команды: \n 1. /say <text> - повторяет фразу <text> \n 2. /list - показывает содержание таблицы sql \n 3. /post - высылает пост (в разработке) \n 4. /teach <команда> <ответ> - обучение бота новым фразам")
# insert_into("answer", "safasdf", "sadfsadg")





