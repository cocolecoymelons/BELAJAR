import sqlite3

connect_db = sqlite3.connect("Customer.db")

db_cursor = connect_db.cursor()

db_cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS customer_order_data(
            
            No INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            product_price Per Unit REAL NOT NULL CHECK(Product Price Per Unit > 0),
            product_detail TEXT NOT NULL,
            total_price REAL NOT NULL CHECK(Total Price > 0)
        )
    
    """);

def add_customer_order_in_sql(cname,pname,pprice,pdetail,total):
    
    db_cursor.execute("INSERT INTO customer_order_data (Customer Name,Product Name,Product Price Per Unit,Product Detail,Total Price) VALUES (?,? ?,?,?)", (cname,pname,pprice,pdetail,total)
    )
    connect_db.commit()
