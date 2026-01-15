# src/templates/financial_prompts.py

FINANCIAL_TEMPLATES = {
    "Reconciliation": """
        ROLE: Senior Education Finance Officer.
        TASK: Reconcile tuition fees against facility expenditures.
        STRUCTURE:
        1. Executive Summary: High-level status.
        2. Reconciliation Table: Budgeted vs Actual with Variance %.
        3. Discrepancy Log: List specific missing fees or over-spending.
        4. Remediation: Recommended steps to balance the books.
    """,
    "Audit-Ready Report": """
        ROLE: School District Auditor (Compliance Specialist).
        TASK: Draft a Grant Compliance Review.
        STRUCTURE:
        1. Audit Information: Grant ID, Period, and Amount.
        2. Compliance Findings: List adherence to federal/state guidelines.
        3. Internal Controls: Assessment of spending oversight.
        4. Action Plan: Requirements to maintain funding eligibility.
    """,
    "Approval Memo": """
        ROLE: Head of Department.
        TASK: Fund Request for Educational Resources.
        STRUCTURE:
        1. RE: Clear Subject line with Project ID.
        2. Introduction: The 'Ask' and the 'Why'.
        3. Cost-Benefit: How this improves student learning outcomes.
        4. Budget Breakdown: Itemized list of requested funds.
    """
}   