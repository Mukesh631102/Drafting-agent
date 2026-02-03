import sys
import os

# Ensure Python can see the 'src' folder
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database_mgr import DatabaseManager

def seed_project():
    print("🚀 Initializing Large-Scale EduFinance Database...")
    db = DatabaseManager()
    
    with db.get_connection() as conn:
        # 1. Clear existing data
        conn.execute("DELETE FROM students")
        conn.execute("DELETE FROM bank_feed")
        conn.execute("DELETE FROM ai_drafts") # Optional: clear history too
        
        # 2. Diverse Student Body (Source of Truth)
        # Total Tuition Due: $74,000
        students = [
            ('S101', 'Alice Johnson', 5000.00),
            ('S102', 'Robert Smith', 4500.00),
            ('S103', 'Vijay Kumar', 5200.00),
            ('S104', 'Diana Prince', 4800.00),
            ('S105', 'Edward Norton', 5000.00),
            ('S106', 'Fiona Gallagher', 4500.00),
            ('S107', 'George Miller', 5500.00),
            ('S108', 'Hannah Abbott', 4800.00),
            ('S109', 'Ian Wright', 5100.00),
            ('S110', 'Jenny Slate', 4900.00),
            ('S111', 'Kevin Hart', 5000.00),
            ('S112', 'Laura Palmer', 4700.00),
            ('S113', 'Mike Ross', 5300.00),
            ('S114', 'Nina Simone', 4600.00),
            ('S115', 'Oscar Isaac', 5000.00)
        ]
        conn.executemany("INSERT INTO students (student_id, name, tuition_due) VALUES (?, ?, ?)", students)

        # 3. Messy Bank Feed (The Audit Challenge)
        # Total Identified: $23,100 | Coverage: ~31%
        bank_entries = [
            ('ALICE J - Q1 FEES', 5000.00, 'unprocessed'),      # Exact Match
            ('ROB SMITH UNIV PMT', 4500.00, 'unprocessed'),    # Exact Match
            ('V. KUMAR / STUDENT FEE', 1200.00, 'unprocessed'),# Partial Match (Vijay owes 5200)
            ('DIANA P TERM 1', 4800.00, 'unprocessed'),        # Name Variation
            ('E. NORTON TRANSFER', 2500.00, 'unprocessed'),    # Partial Payment
            ('F GALLAGHER EFT', 4500.00, 'processed'),       # Initials Variation
            ('UNKNOWN REF 9920', 600.00, 'processed'),       # Forensic Mystery
            ('G. MILLER FINANCE', 5500.00, 'processed'),     # Large Payment
            ('MISC DEPOSIT SCHOOL', 100.00, 'unprocessed'),    # Small Noise
            ('ISAAC O - OVERPAYMENT', 5500.00, 'unprocessed')  # Overpayment (Oscar owes 5000)
        ]
        conn.executemany("INSERT INTO bank_feed (payer_name, amount, status) VALUES (?, ?, ?)", bank_entries)
        
        conn.commit()
    
    print("✅ Large Database Seeded Successfully!")
    print(f"📊 Ready to analyze {len(students)} students and {len(bank_entries)} bank records.")

if __name__ == "__main__":
    seed_project()