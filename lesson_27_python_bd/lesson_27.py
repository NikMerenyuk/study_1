import pandas
import sqlite3

connection = sqlite3.connect('sample.db')

cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS products (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        price real,
        amount integer DEFAULT '0'        
    )
    '''
)

# first way
# cursor.execute(
#     '''
#     INSERT INTO products (name, price, amount)
#     VALUES (?, ?, ?)
#     ''', ('apple', 100, 5)
# )

# second way
# cursor.execute(
#     '''
#     INSERT INTO products (name, price, amount)
#     VALUES (:name, :price, :amount)
#     ''', {'name': 'banana', 'price': 150, 'amount': 4}
# )


# products = [
#     [f'product {i}', i * 100, i] for i in range(100)
# ]
#
# for i_products in products:
#     cursor.execute(
#         '''
#         INSERT INTO products (name, price, amount)
#         VALUES (:name, :price, :amount)
#         ''', {'name': i_products[0], 'price': i_products[1], 'amount': i_products[2]}
#     )


query = cursor.execute('''SELECT * FROM products''')

data_frame = pandas.DataFrame(query.fetchall(), columns=[
    'Id', 'Name', 'Price', 'Amount'
])
print(data_frame)
# print(query.fetchall())


connection.commit()

connection.close()
