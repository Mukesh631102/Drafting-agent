# src/database/db_logic.py
import sqlite3
import pandas as pd
import os

class DatabaseManager:
    def __init__(self):
        # Path to the DB in the instance folder
        self.db_path = os.path.join("instance", "edufinance.db")
        os.makedirs("instance", exist_ok=True)
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def init_db(self):
        with self.get_connection() as conn:
            # Table for Student Records
            conn.execute("""CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY, 
                name TEXT, 
                tuition_due REAL)""")
            # Table for Messy Bank Feeds
            conn.execute("""CREATE TABLE IF NOT EXISTS bank_feed (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payer_name TEXT, 
                amount_received REAL, 
                status TEXT DEFAULT 'unprocessed')""")
            # Table for AI Audit History
            conn.execute("""CREATE TABLE IF NOT EXISTS ai_drafts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT, 
                content TEXT, 
                reflection TEXT,
                status TEXT DEFAULT 'draft')""")

    def get_unprocessed_df(self):
        with self.get_connection() as conn:
            return pd.read_sql_query("SELECT * FROM bank_feed WHERE status='unprocessed'", conn)