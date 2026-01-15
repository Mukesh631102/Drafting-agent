import sys
import os

# Ensure the script can see the 'src' folder
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database_mgr import DatabaseManager

def seed():
    print("🚀 Initializing Database Seeding...")
    db = DatabaseManager()
    
    with db.get_connection() as conn:
        # 1. Clear old data to start fresh (Optional for testing)
        conn.execute("DELETE FROM students")
        conn.execute("DELETE FROM bank_feed")
        conn.execute("DELETE FROM agent_logs")

        # 2. Add Master Student Records
        students = [
            ('STU-101', 'Alice Johnson', 'alice@email.com', 1500.00),
            ('STU-102', 'Bob Smith', 'bob@email.com', 2000.00),
            ('STU-103', 'Charlie Brown', 'charlie@email.com', 1200.00)
        ]
        conn.executemany("INSERT INTO students (student_id, name, email, tuition_due) VALUES (?, ?, ?, ?)", students)

        # 3. Add Bank Transactions for the Agent to "Analyze"
        # Notice how 'Alice J.' doesn't perfectly match 'Alice Johnson' - tests the AI!
        transactions = [
            ('Alice J.', 500.00, 'unprocessed'),
            ('Robert Smith', 2000.00, 'unprocessed'),
            ('C. Brown', 100.00, 'unprocessed')
        ]
        conn.executemany("INSERT INTO bank_feed (payer_name, amount_received, status) VALUES (?, ?, ?)", transactions)
        
        conn.commit()
    
    print("✅ Database successfully seeded with 3 students and 3 transactions!")

if __name__ == "__main__":
    seed()