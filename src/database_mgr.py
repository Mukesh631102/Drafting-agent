import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path='instance/edufinance.db'):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row 
        return conn

    def init_db(self):
        """Initializes an advanced schema for autonomous auditing."""
        with self.get_connection() as conn:
            # 1. Master Student Records (Source of Truth)
            conn.execute('''CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT,
                tuition_due REAL DEFAULT 0.0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')

            # 2. Bank Transactions (The Perception Module)
            conn.execute('''CREATE TABLE IF NOT EXISTS bank_feed (
                txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
                payer_name TEXT,
                amount_received REAL,
                txn_date DATE,
                status TEXT DEFAULT 'unprocessed', -- 'unprocessed', 'matched', 'flagged'
                confidence_score REAL DEFAULT 0.0
            )''')

            # 3. AI Drafting & Reflection Memory (The Output)
            conn.execute('''CREATE TABLE IF NOT EXISTS ai_drafts (
                draft_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                draft_type TEXT, -- 'reminder', 'receipt', 'warning'
                content TEXT,
                status TEXT DEFAULT 'pending_review', -- 'pending_review', 'approved', 'rejected'
                reflection_notes TEXT, -- The "Self-Correction" feedback
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(student_id)
            )''')

            # 4. Agentic Audit Log (The Accountability Trace)
            conn.execute('''CREATE TABLE IF NOT EXISTS agent_logs (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT, -- e.g., 'analyzing_transaction', 'generating_draft'
                details TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
            conn.commit()

    # --- EXPERT METHODS FOR THE AGENT ---

    def log_agent_action(self, action, details):
        """Records the agent's internal reasoning for the UI."""
        with self.get_connection() as conn:
            conn.execute("INSERT INTO agent_logs (action, details) VALUES (?, ?)", (action, details))
            conn.commit()

    def get_next_task(self):
        """The 'Perception' step: finds the first unprocessed transaction."""
        with self.get_connection() as conn:
            return conn.execute("SELECT * FROM bank_feed WHERE status = 'unprocessed' LIMIT 1").fetchone()

    def save_draft_with_reflection(self, student_id, content, reflection):
        """The 'Action + Reflection' step: saves draft and the agent's self-critique."""
        with self.get_connection() as conn:
            conn.execute('''
                INSERT INTO ai_drafts (student_id, content, reflection_notes) 
                VALUES (?, ?, ?)
            ''', (student_id, content, reflection))
            conn.commit()