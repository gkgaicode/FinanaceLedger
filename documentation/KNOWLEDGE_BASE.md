# 📖 Business Logic & Technical Knowledge Base

This document details the underlying financial formulas, architectural specifications, and structural paradigms required to operate or rebuild the Indian Personal Finance Engine.

## 1. Business Logic Mapping: QuickBooks to Personal Finance
To bridge business enterprise tools with everyday consumer budgeting, commercial concepts are mapped directly to personal finance equivalents:
* **Chart of Accounts:** Translates corporate categories into personal buckets (Assets = Bank/Investments, Liabilities = Loans/Credit Cards, Income = Gross Salary, Expenses = Living/Taxes).
* **Accounts Receivable:** Re-engineered as a **Corporate Reimbursement Pipeline** tracking pending workplace employee claims (e.g., fuel, internet, medical allowances).
* **Double-Entry Rule (Debits = Credits):** Every financial movement generates balancing journal split lines. For instance, receiving a salary debits Bank (Asset increases) and debits TDS Account (Expense increases), while crediting Salary Revenue (Income increases). Net sum of a transaction must always equal zero.

## 2. Indian Income Tax Engine Specifications (FY 2026-27 / AY 2027-28)
The core engine computes tax liability under both Indian tax tracks dynamically to maximize consumer monthly cash take-home levels.

### A. House Rent Allowance (HRA) Exemption Logic
The script calculates HRA exemption by isolating the *minimum* of three distinct legal parameters:
1. Actual HRA component received from the employer's salary structure break-out.
2. Actual Rent Paid minus 10% of the User's Basic Pay.
3. 50% of Basic Pay (if living in an identified Metro city like Mumbai, Delhi, Kolkata, Chennai, Hyderabad, Bengaluru) or 40% of Basic Pay for Non-Metro zones.

### B. Tax Regimes Breakdown Matrix
* **Old Regime Rules:** Preserves standard itemized deductions. Includes a ₹50,000 standard deduction, Section 80C caps clamped tightly at ₹1,50,000 (PPF, ELSS, EPF), Section 80D medical premium allowance limits capped at ₹25,000, and full HRA exemptions. Income under ₹5,000,000 receives a Section 87A rebate (zero net tax).
* **New Regime Rules:** Maximizes standard bracket allowances but strips itemized deductions. Provides a raised standard deduction of ₹75,000. Incorporates structural tax bands starting at 5% over ₹3,00,000, progressing in steps up to a 30% ceiling terminal rate. Income under ₹7,00,000 receives full structural Section 87A rebate protection.
* **Health & Education Cess:** A flat 4% multiplier applies directly over the final calculated base tax liability across both tracks.

## 3. Real-Time Data Ingestion Specifications

### A. Android Transactional SMS Formatting (India)
Indian banking structures route near-instantaneous notification messages via shortcodes (e.g., `AD-HDFCBK`). The ingestion regex engine must capture and process text variations handling parameters such as:
* **Currency Modifiers:** Handles `Rs.`, `RS`, `INR`.
* **Account Tracking Hooks:** Extracts account tail endings using patterns matching trailing integers following indicators like `A/c`, `Card`, or `Ending`.
* **Action Types:** Distinguishes outlays (`Debited`, `Spent`, `Paid`) from inflows (`Credited`).
* **Merchant Tracking:** Isolates VPA patterns and UPI markers using regex text processing boundary sweeps.

### B. ReBIT Account Aggregator Schema
Data collection pipelines pull consent-based banking payloads matching official ReBIT JSON structures containing:
* Cryptographic signature hashes to verify data source provenance.
* Unique transaction tracker identifiers mapping to a strict `reference` key field to fully block database duplication attacks.
* Standardized `DEBIT`/`CREDIT` indicators matching explicit timestamp keys.
