import sqlite3

connect = sqlite3.connect('db_test.sqlite')
cur = connect.cursor()

def get_all():
    cur.execute("SELECT * FROM owners")
    result = cur.fetchall()
    for i in range(len(result)):
        print(result[i])

    cur.execute("SELECT * FROM models")
    result = cur.fetchall()
    for i in range(len(result)):
        print(result[i])

    cur.execute("SELECT * FROM cars")
    result = cur.fetchall()
    for i in range(len(result)):
        print(result[i])

def get_mark(obj):
    cur.execute(f"SELECT * FROM models WHERE mark = {obj}")
    result = list(cur.fetchall())

    for i in range(len(result)):
        print(list(result[i]))

def get_mark_and_color():
    pass

get_mark('Toyota')



connect.commit()
connect.close()

