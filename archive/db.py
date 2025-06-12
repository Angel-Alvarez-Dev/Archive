# archive/db.py

import sqlite3

DB_PATH = "emails.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL
            );
        """)

def save_email(email: str) -> bool:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO emails (email) VALUES (?)", (email,))
        return True
    except sqlite3.IntegrityError:
        return False
