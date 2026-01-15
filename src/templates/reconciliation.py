RECON_TEMPLATE = """
# MONTHLY FINANCIAL RECONCILIATION
**Department:** Education - Finance Office
**Reporting Month:** {month}

## 1. RECONCILIATION SUMMARY
Total Budgeted: {budgeted}
Total Actual: {actual}
**NET VARIANCE:** {variance}

## 2. LINE ITEM ANALYSIS
{line_items}

## 3. UNRESOLVED DISCREPANCIES
- {discrepancy_1}
- {discrepancy_2}

**Authorized by:** ____________________
"""