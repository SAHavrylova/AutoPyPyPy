import sqlite3


class Database():
    
    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/sa/AutoPyPyPy' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()
    
    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected succesfully. SQLite Database Version is {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()
    
    def delete_product_by_id(self,product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_all_code(self):
        query = "SELECT postalCode FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_address_by_postal_code(self, postalCode):
        query = f"SELECT address, postalCode FROM customers WHERE postalCode = '{postalCode}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 
      
    def get_all_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_postal_code_to_customer(self, id, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, city, postalCode, country)\
            VALUES ({id}, '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_all_customers_id(self):
        query = "SELECT id FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_city_and_postalCode(self, city, postalCode):
        query = f"SELECT city, postalCode FROM customers WHERE city = '{city}' AND postalCode = '{postalCode}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def delete_code_by_id(self, id):
        query = f"DELETE FROM customers WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def update_postal_code_by_city_and_id(self, id, city, postalCode):
        query = f"UPDATE customers SET postalCode = '{postalCode}' WHERE id = {id} AND city = '{city}'"
        self.cursor.execute(query)
        self.connection.commit()
    

    