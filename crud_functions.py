import sqlite3

connection = sqlite3.connect('db_bot.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


initiate_db()

# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
#                    (f'Продукт_№{i}', f'описание_{i}', f'{i * 100}'))
# connection.commit()