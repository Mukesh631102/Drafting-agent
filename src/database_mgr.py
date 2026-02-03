import sqlite3
import os
import pandas as pd

class DatabaseManager:
    def __init__(self, db_name="edufinance.db"):
        # Points to the 'instance' folder in your project root
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(self.base_dir, "instance", db_name)
        
        # Ensure the instance folder exists for the .db file
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def init_db(self):
        with self.get_connection() as conn:
            # 1. Master Student List
            conn.execute("""CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY, name TEXT, tuition_due REAL)""")
            
            # 2. Incoming Bank Transactions
            conn.execute("""CREATE TABLE IF NOT EXISTS bank_feed (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payer_name TEXT, amount REAL, status TEXT DEFAULT 'unprocessed')""")
            
            # 3. AI Generated Reports
            conn.execute("""CREATE TABLE IF NOT EXISTS ai_drafts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT, content TEXT, reflection TEXT, status TEXT DEFAULT 'draft')""")
            conn.commit()

    def get_unprocessed_df(self):
        with self.get_connection() as conn:
            return pd.read_sql_query("SELECT * FROM bank_feed WHERE status='unprocessed'", conn)

    def save_draft_with_reflection(self, student_id, content, reflection):
        with self.get_connection() as conn:
            conn.execute("INSERT INTO ai_drafts (student_id, content, reflection) VALUES (?, ?, ?)", 
                         (student_id, content, reflection))
            conn.commit()