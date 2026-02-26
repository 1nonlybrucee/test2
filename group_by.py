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
        print(f'Total: {result[0]} = {result[1]}')
    
    results = cursor.execute('SELECT product_name, COUNT(sales_id), SUM(quantity) FROM sales GROUP BY product_name')
    for result in results:
        print(f'total transaction: {result[0]} = {result[1]}\n total sold: {result[2]}')

    haha = cursor.execute('SELECT strftime("%Y-%m", sales_date) as month, SUM(quantity * price) as total_revenue FROM sales GROUP BY month')
    for hah in haha:
        print(f'Month: {hah[0]} - REVENUE: {hah[1]}')