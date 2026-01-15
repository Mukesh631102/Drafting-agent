# src/templates/approval_memo.py

APPROVAL_MEMO_TEMPLATE = """
# MEMORANDUM OF APPROVAL: FUND REQUEST
**TO:** {recipient_name} ({recipient_title})
**FROM:** {sender_name} ({sender_title})
**DATE:** {date}
**SUBJECT:** {subject}

---

## 1. PURPOSE OF REQUEST
{purpose_statement}

## 2. JUSTIFICATION & EDUCATIONAL IMPACT
* **Need:** {problem_statement}
* **Benefit:** {learning_outcomes}
* **Alignment:** {strategic_alignment} (How this fits the school's mission)

## 3. BUDGET & COST BREAKDOWN
| Item Description | Unit Cost | Quantity | Total |
| :--- | :--- | :--- | :--- |
{budget_table}

**TOTAL REQUESTED AMOUNT:** {total_amount}

## 4. IMPLEMENTATION TIMELINE
* **Phase 1:** {phase_1}
* **Phase 2:** {phase_2}

## 5. APPROVAL SIGNATURES
**Department Head:** ____________________  **Date:** __________
**Finance Office:** ____________________  **Date:** __________
"""