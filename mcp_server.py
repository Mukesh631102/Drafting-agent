import sqlite3
import os
import sys
from mcp.server.fastmcp import FastMCP

# This prevents any accidental prints from breaking the protocol
sys.stdout.reconfigure(encoding='utf-8')

mcp = FastMCP("EduFinance_ERP")

@mcp.tool()
def get_ledger_record(payer_name: str):
    """Retriever Agent: Fetches grounded financial data."""
    # Robust pathing for SQLite
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "data", "edufinance.db")
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ai_drafts LIMIT 1") # Simplified for testing
        row = cursor.fetchone()
        conn.close()
        
        return str(dict(row)) if row else "No data found."
    except Exception as e:
        # Errors sent to stderr won't break the JSON-RPC connection
        sys.stderr.write(f"Log: Database error - {str(e)}\n")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()