import sqlite3

DB_name = "weeklyprice.db"

def create_save_database(ticker: str, weekly_price: list) -> None:

    table_name = f"{ticker.upper()}_price"
    
    with sqlite3.connect(DB_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE if NOT EXISTS {table_name} (
                date TEXT PRIMARY KEY,
                price REAL 
            ) 
        """)

        cursor.executemany(f"""
            INSERT OR IGNORE INTO {table_name} (date, price)
            VALUES (?, ?) 
        """, (
            [(str(week.date), week.price) for week in weekly_price]
        ))

def get_data_db (ticker: str) -> list:
    table_name = f"{ticker.upper()}_price"
    return_list = []

    with sqlite3.connect(DB_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT *
            FROM {table_name}
        """)
        return_list = cursor.fetchall()
        return return_list 