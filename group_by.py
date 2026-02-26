import sqlite3

with sqlite3.connect('group_by.db') as connection:
    cursor = connection.cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS sales (
            sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            category TEXT,
            quantity INTEGER,
            price REAL,
            sales_date TEXT DEFAULT CURRENT_TIMESTAMP
        )'''
    )

    results = cursor.execute('SELECT product_name, SUM (quantity * price) FROM sales GROUP BY product_name')
    for result in results:
        print(f'Product: {result[0]} = {result[1]}')