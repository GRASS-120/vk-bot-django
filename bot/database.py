import sqlite3

# Подключение к БД
connect = sqlite3.connect('db.sqlite')
# Создание курсора
cur = connect.cursor()

# Создание запроса
# query = """
# CREATE TABLE phonebook(
#     id INT PRIMARY KEY,
#     name TEXT,
#     p_number INT
# );
# """

# Добавление значений в таблицу
# query = """
# INSERT INTO phonebook (id, name, p_number) VALUES (0, 'Ярик', 88005553535);
# """

# Добавление значений в таблицу
# query = """
# INSERT INTO phonebook (id, name, p_number) VALUES
# (1, 'Максим', 88005553535),
# (2, 'Хыч', 88005553535),
# (3, 'Егор', 88005553535),
# (4, 'Святополк', 88005553535);
# """

# Выборка
# query = """
# SELECT * FROM phonebook
# """

# query = """
# CREATE TABLE answer(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     msg TEXT,
#     answ TEXT
# );
# """

query = """
INSERT INTO answer(msg, answ) VALUES
('/start', 'Бот-вк начинает работу! 🤖'),
('/post', 'Вот пост:')
"""

# query = "UPDATE answer SET answ = 'Бот-вк начинает работу! 🤖\n Доступные команды: \n 1. /say <text> - повторяет фразу <text> \n 2. /list - показывает содержание таблицы sql \n 3. /post - высылает пост (в разработке)' WHERE id = 1"

# Выполнение запроса
cur.execute(query)

# Выводит данные
result = cur.fetchall()
print(result)

# Сохранение состояние БД
connect.commit()

# Выход из таблицы
connect.close()