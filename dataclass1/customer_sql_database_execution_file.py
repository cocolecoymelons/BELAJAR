import sqlite3

connect_db = sqlite3.connect("Customer.db")

db_cursor = connect_db.cursor()

db_cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS customer_order_data(
            
            No INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            product_price REAL NOT NULL CHECK(  product_price > 0),
            product_detail TEXT NOT NULL,
            total_price REAL GENERATED ALWAYS AS (quantity * product_price) STORED
        )
    
    """);

def save_customer_orders_in_db(cname,pname,quanty,pprice,pdetail):
    
    db_cursor.execute("INSERT INTO customer_order_data (customer_name,product_name,quantity,product_price,product_detail) VALUES (?,?,?,?,?)", (cname,pname,quanty,pprice,pdetail)
    )
    connect_db.commit()
    
def update_customer_order(cname,pname,quanty,pprice,pdetail,no):
    
    db_cursor.execute("""
        UPDATE customer_order_data
        SET customer_name = ?, product_name = ?, quantity = ?, product_price = ?, product_detail = ?
        WHERE no = ?
    """,(cname,pname,quanty,pprice,pdetail,no)
    )
    
    connect_db.commit()
    
    return db_cursor.rowcount > 0
