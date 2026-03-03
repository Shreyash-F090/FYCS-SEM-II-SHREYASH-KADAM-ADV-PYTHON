import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("store.db")
        self.cursor = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, stock INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, role TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS sales_history (sale_id INTEGER PRIMARY KEY AUTOINCREMENT, p_name TEXT, qty INTEGER, total REAL)")
        self.cursor.execute("INSERT OR IGNORE INTO users VALUES ('shreyash', 'F090', 'admin')")
        self.conn.commit()

    def authenticate(self, user, pwd):
        self.cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (user, pwd))
        return self.cursor.fetchone()

    def get_products(self, search=""):
        if search:
            self.cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + search + '%',))
        else:
            self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def update_stock(self, p_id, qty):
        self.cursor.execute("UPDATE products SET stock = stock + ? WHERE id = ?", (qty, p_id))
        self.conn.commit()

    def add_product(self, name, price, stock):
        self.cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
        self.conn.commit()

    def process_sale(self, p_id, qty):
        self.cursor.execute("SELECT name, price, stock FROM products WHERE id=?", (p_id,))
        item = self.cursor.fetchone()
        if item and item[2] >= qty:
            total = item[1] * qty
            self.cursor.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (qty, p_id))
            self.cursor.execute("INSERT INTO sales_history (p_name, qty, total) VALUES (?, ?, ?)", (item[0], qty, total))
            self.conn.commit()
            return True
        return False

    def delete_product(self, p_id):
        self.cursor.execute("DELETE FROM products WHERE id=?", (p_id,))
        self.conn.commit()

    def get_revenue(self):
        self.cursor.execute("SELECT SUM(total) FROM sales_history")
        res = self.cursor.fetchone()
        return res[0] if res[0] else 0.0
