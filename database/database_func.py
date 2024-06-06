import sqlite3 as sql


def add_entry(link, name, old):
    with sql.connect(link) as connect:
        cur = connect.cursor()
        cur.execute('''INSERT INTO table_1 VALUES (NULL, ?, ?)''',
                    (name, old))


def select_entry(link, id):
    with sql.connect(link) as connect:
        cur = connect.cursor()
        cur.execute('''SELECT name FROM table_1 WHERE id = :id''',
                    {'id': id})
        result = cur.fetchall()
        return result