import sqlite3

def init_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Drop old tables (optional for reset)
    c.execute("DROP TABLE IF EXISTS stock")
    c.execute("DROP TABLE IF EXISTS warehouse")

    # Create warehouse table
    c.execute('''
        CREATE TABLE warehouse (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    # Create stock table
    c.execute('''
        CREATE TABLE stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT,
            rfid TEXT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            warehouse_id INTEGER,
            FOREIGN KEY (warehouse_id) REFERENCES warehouse(id)
        )
    ''')

    # Optional: Insert a default warehouse
    c.execute("INSERT INTO warehouse (name) VALUES (?)", ("Main Warehouse",))

    conn.commit()
    conn.close()
    print("✅ inventory.db initialized successfully.")
