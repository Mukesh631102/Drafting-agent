**TUITION ACCRUAL – BANK DEPOSIT RECONCILIATION**  
**Period Covered:** 5 January 2026 – 12 January 2026  

**Prepared by:** Chief Financial Officer’s Office  
**Date:** 14 January 2026  
**Version:** 1.0  

---

### 1. Objective  
To confirm that all tuition‑related accruals recorded in the Internal Tuition Ledger (Source A) are reflected in the Bank Deposit Statement (Source B) for the period 5 Jan 2026 – 12 Jan 2026, and to quantify any variances, missing entries, or classification issues.

### 2. Scope & Data Sources  

| Source | Description | Record Count |
|--------|-------------|--------------|
| **Source A – Internal Tuition Ledger (Accrual)** | Pending tuition items (IDs STU‑8821, STU‑9902, STU‑4410, STU‑1125, STU‑5501) | 5 |
| **Source B – Bank Deposit Statement (Cash)** | Deposit entries (Refs DEP‑001 through DEP‑005) | 5 |

### 3. Reconciliation Methodology  

1. **Match‑by‑ID/Reference** – Align each ledger entry with the corresponding bank deposit using student name, amount, and date.  
2. **Variance Analysis** – Compute amount differences for matched pairs.  
3. **Residual Review** – Identify any ledger items without a deposit match and any deposits without a ledger counterpart.  

### 4. Matching Summary  

| Ledger ID (Source A) | Payer / Description | Accrued Fee | Deposit Ref (Source B) | Deposited Amount | Variance |
|----------------------|---------------------|------------|------------------------|------------------|----------|
| STU‑8821 | James Wilson | $5,400.00 | DEP‑001 | $5,400.00 | $0.00 |
| STU‑9902 | Maria Garcia | $5,400.00 | DEP‑002 | $5,350.00 | **‑$50.00** |
| STU‑4410 | TechCorp Scholarship | $12,000.00 | DEP‑003 | $12,000.00 | $0.00 |
| STU‑1125 | Robert Chen | $5,400.00 | DEP‑004 | $5,400.00 | $0.00 |
| STU‑5501 | Sarah Jenkins (Lab Fee) | $2,100.00 | DEP‑005 | $2,100.00 | $0.00 |

### 5. Variance & Exception Detail  

#### 5.1 Maria Garcia – $50.00 Shortfall  
- **Observation:** Deposit DEP‑002 is $50.00 less than the accrued fee.  
- **Root Cause:** A wire‑transfer fee of $50.00 was deducted by the bank (noted on the deposit slip).  
- **Impact:** The ledger does not presently record this bank‑service charge, resulting in a net variance of –$50.00.

#### 5.2 STU‑5501 – “UNKNOWN” Payer  
- **Observation:** Deposit DEP‑005 is recorded with payer “UNKNOWN” but matches the $2,100.00 lab‑fee accrual for Sarah Jenkins.  
- **Root Cause:** The payer field was left blank during cash‑receipt entry, suggesting a third‑party payment (e.g., parent, scholarship, or cash receipt) that was not captured in the ledger.  
- **Impact:** Absence of payer identification may affect revenue attribution, cost allocation, and compliance with scholarship or grant reporting requirements.

#### 5.3 Missing or Unmatched Entries  
- All five ledger items have corresponding deposit entries.  
- No deposit entries remain unmatched after allocating the “UNKNOWN” deposit to STU‑5501.

### 6. Mathematical Consistency Check  

| Metric | Amount |
|--------|--------|
| Total Accrued Tuition (Source A) | $30,300.00 |
| Total Deposited Cash (Source B) | $30,250.00 |
| Net Variance | **‑$50.00** |

The net variance aligns precisely with the $50.00 wire‑fee shortfall identified for Maria Garcia.

### 7. Potential Budget Discrepancies  

1. **Unrecorded Bank‑Fee Expense – $50.00**  
   - Should be booked to “Bank Service Charges” (or an equivalent expense account) to reconcile the variance.  

2. **Unidentified Payer for Lab Fee – $2,100.00**  
   - Lack of payer attribution may distort revenue tracking and affect scholarship/grant reporting.  

### 8. Strategic Alignment Assessment  

| Area | Assessment |
|------|------------|
| **Revenue Recognition** | Accurate matching of accruals to cash receipts is essential for reliable financial statements and accreditation compliance. |
| **Scholarship Accounting** | The TechCorp scholarship is correctly recorded; no variance detected. |
| **Operational Controls** | The $50 wire‑fee and “UNKNOWN” payer highlight opportunities to strengthen cash‑receipt processing (mandatory payer field validation, automated fee capture). |
| **Budget Forecasting** | The $50 variance represents 0.16 % of total tuition revenue – immaterial, yet correction is required for forecast precision. |

### 9. Recommendations / Action Items  

| # | Action | Owner | Due Date |
|---|--------|-------|----------|
| 1 | Record a $50.00 bank‑service‑charge expense in the General Ledger (account “Bank Service Charges”). | Accounting Manager | 20 Jan 2026 |
| 2 | Amend the Internal Tuition Ledger to capture the payer for the $2,100.00 lab‑fee deposit (STU‑5501) and investigate the source of the “UNKNOWN” label. | Tuition Billing Supervisor | 31 Jan 2026 |
| 3 | Update the Cash‑Receipt Standard Operating Procedure to require explicit payer identification and automatic deduction of known bank fees. | Finance Operations Lead | 15 Feb 2026 |
| 4 | Perform a follow‑up reconciliation for February 2026 to verify implementation of corrective actions. | CFO Office | 15 Mar 2026 |

### 10. Key Findings  

- **Complete Match:** All five tuition accruals have corresponding bank deposits; no missing tuition items.  
- **$50 Discrepancy:** Maria Garcia’s deposit is $50 short due to a wire‑transfer fee; ledger lacks a corresponding expense entry.  
- **Unknown Payer:** Deposit for Sarah Jenkins’s lab fee lacks payer identification, indicating a data‑entry lapse.  
- **Mathematical Consistency:** Aggregate tuition accruals ($30,300) exceed cash deposits ($30,250) by $50, confirming the isolated variance.  
- **Control Weaknesses:** Absence of payer identification and omission of bank‑fee recording expose the institution to misstatement risk.  

### 11. Conclusion  

The reconciliation confirms that tuition accruals for the period are fully reflected in cash receipts, with a single, immaterial variance attributable to a bank‑service charge and a data‑entry omission concerning payer identification. Prompt execution of the recommended actions will eliminate the identified control gaps, ensure accurate expense classification, and reinforce compliance with institutional and accreditation standards.

---  

**Prepared by:** _______________________  
Chief Financial Officer  

**Reviewed and Approved by:** _______________________  
Vice President, Finance & Administration  

*End of Document*