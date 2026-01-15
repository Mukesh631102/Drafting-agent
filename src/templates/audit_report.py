AUDIT_TEMPLATE = """
# COMPLIANCE AUDIT REPORT: [Grant Name/Project]
**Date:** {date}
**Auditor:** Gemini AI Finance Agent

## 1. EXECUTIVE SUMMARY
{summary}

## 2. GRANT COMPLIANCE TABLE
| Requirement | Status | Findings |
| :--- | :--- | :--- |
| Documentation | [Pass/Fail] | {doc_findings} |
| Budget Adherence | [Pass/Fail] | {budget_findings} |

## 3. INTERNAL CONTROLS ASSESSMENT
{assessment}

## 4. CORRECTIVE ACTION PLAN
- [ ] Task 1: {task_1}
- [ ] Task 2: {task_2}
"""