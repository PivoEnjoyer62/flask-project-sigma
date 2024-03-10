import sqlite3


class SQLManager:
    def __init__(self, db_name):
        self.sql = sqlite3.connect(f"{db_name}.db")

    def create_tables(self):
        db_cursor = self.sql.cursor()
        db_cursor.execute(f""" 
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            nickname TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
