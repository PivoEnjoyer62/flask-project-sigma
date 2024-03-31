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

    def create_articles_table(self):
        db_cursor = self.sql.cursor()
        db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Articles (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            text TEXT NOT NULL
        )
        """)
        db_cursor.close()
        self.sql.commit()

    def insert_articles(self, title, text):
        db_cursor = self.sql.cursor()
        db_cursor.execute(f"""
        INSERT INTO Articles(title, text) VALUES(?, ?)
        """, [title, text])
        db_cursor.close()
        self.sql.commit()

    def select_articles(self):
        db_cursor = self.sql.cursor()
        db_cursor.execute(f"""
        SELECT title, text FROM Articles;
        """)
        data = db_cursor.fetchall()
        db_cursor.close()
        self.sql.commit()
        return data

    def get_user_by_id(self, id):
        db_cursor = self.sql.cursor()
        db_cursor.execute(f"""
        SELECT * FROM Users WHERE id=?
        """, [id])
        db_cursor.close()
        self.sql.commit()
