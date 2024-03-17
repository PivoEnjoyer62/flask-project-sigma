import sqlite3


class SQLManager:
    def __init__(self, db_name):
        self.sql = sqlite3.connect(f"{db_name}.db")

    def create_table_users(self):
        db_cursor = self.sql.cursor()
        db_cursor.execute(f""" 
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            nickname TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        db_cursor.close()
        self.sql.commit()

    def register_insertion(self, nickname, email, password):
        db_cursor = self.sql.cursor()
        db_cursor.execute(f"""
        INSERT INTO Users(nickname, email, password) VALUES(?, ?, ?)
        """, [nickname, email, password])
        db_cursor.close()
        self.sql.commit()

    def login_selection(self, email, password):
        db_cursor = self.sql.cursor()
        db_cursor.execute(f"""
        SELECT email, password FROM Users WHERE email=? AND password=?
        """, [email, password])
        data = db_cursor.fetchone()
        db_cursor.close()
        self.sql.commit()

        return data

