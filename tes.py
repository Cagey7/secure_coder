import sqlite3

def get_products_in_price_range(min_price, max_price):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    sql_query = "SELECT * FROM products WHERE price >= ? AND price <= ?"
    cursor.execute(sql_query, (min_price, max_price))
    results = cursor.fetchall()
    connection.close()

    return results

min_price = 10
max_price = 50
products = get_products_in_price_range(min_price, max_price)

if products:
    for product in products:
        print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
else:
    print("No products found in the specified price range.")
