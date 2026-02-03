import mcp.server.fastmcp as fastmcp

# Initialize FastMCP
mcp = fastmcp.FastMCP("EduFinance_Mock")

@mcp.tool()
def fetch_ledger():
    """Returns a mock ledger record for testing."""
    return {
        "payer_name": "Probir Mukherjee",
        "amount": 500.00,
        "status": "unprocessed",
        "student_id": "STU-992"
    }

if __name__ == "__main__":
    # This starts the server in stdio mode by default
    mcp.run()