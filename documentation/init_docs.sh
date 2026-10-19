#!/bin/bash

# Create the target documentation directory layout
mkdir -p documentation

# 1. Generate documentation/README.md
cat << 'EOF' > documentation/README.md
# 🇮🇳 Indian Salaried Personal Finance Core Ledger Engine

An industrial-grade, double-entry financial ledger and real-time transaction processing ecosystem customized specifically for the Indian salaried class. This system mirrors enterprise accounting frameworks (like Intuit QuickBooks) and translates business constructs into automated consumer personal finance engines utilizing **India's Account Aggregator (AA) network, Android real-time SMS triggers, and the dual-regime Income Tax optimization architecture**.

## 🏗️ Core Architecture Overview
The platform uses a decoupled, high-throughput microservices architecture:
1. **Flutter Mobile Client:** Hosts an on-device Android background listener to instantly catch, filter, and transmit raw transactional banking text data alongside a secure Account Aggregator WebView integration module.
2. **FastAPI Ingestion Gateway:** Asynchronous Python web framework validating API keys, running high-performance string parsing algorithms, and routing transactional telemetry into the system engine.
3. **Double-Entry Reconciliation Ledger:** A strict relational database infrastructure designed on ACID properties inside PostgreSQL to secure transactional integrity down to the *paisa*.
4. **Tax Calculation Microservice:** A real-time engine processing Section 80C, 80D, and HRA profiles to optimize user net cash take-home pay structures.

## 🚀 Local Deployment Quickstart

### Prerequisites
* Docker & Docker Compose (v2.0+) installed on the host platform.
* Python 3.11+ (for local workspace compilation).
* Flutter SDK (3.10+) configured with Android target layers.

### Step 1: Clone and Infrastructure Boot
Run the production multi-container environment via Docker Compose from the root workspace directory:
```bash
docker-compose up --build -d
```

### Step 2: Backend Dependency Setup (Development Mode)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Flutter Dependency Sync
```bash
cd ../mobile
flutter pub add http
flutter pub get
```

## 🔒 Security & Compliance
Operating a financial data application in India requires strict adherence to security architectures specified by the **RBI (Reserve Bank of India)** and **CERT-In**:
* **SSL Pinning Execution:** Hardcoded backend public key certificate SHA-256 fingerprints inside the client-side network repository layers to mitigate Man-in-the-Middle (MITM) attacks.
* **PII Encryption Boundaries:** Columns holding clear text identity pointers (PAN, Aadhaar references, phone profiles) are encrypted at rest using AES-256-GCM configurations driven by an enterprise Cloud Key Management Service (KMS).
EOF

# 2. Generate documentation/KNOWLEDGE_BASE.md
cat << 'EOF' > documentation/KNOWLEDGE_BASE.md
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
EOF

# 3. Generate documentation/AGENT_INSTRUCTIONS.md
cat << 'EOF' > documentation/AGENT_INSTRUCTIONS.md
# 🤖 AI Agent Execution Instructions

**Role:** You are an expert FinTech software engineer and systems architect specializing in Indian banking systems, double-entry accounting configurations, and FastAPI/Flutter application setups.

**Objective:** Use this context prompt to generate a production-ready personal accounting app backend and mobile interface client matching the engineering guidelines below.

---

## 1. System Engineering Constraints

### Technology Stack Definition
* **Backend Framework:** Python 3.11 with FastAPI (Uvicorn web workers configuration).
* **Database Target:** PostgreSQL 15+ enforcing structured Relational Double-Entry schemas.
* **Task Management Queue:** Celery workers backed by a Redis key-value broker cache.
* **Mobile Client Framework:** Flutter cross-platform mobile SDK using native HTTP connections.
* **Container Layer:** Docker and Multi-stage target configurations.

### Database Design Rules
* Every financial transaction record must implement double-entry bookkeeping rules.
* Transaction entry operations must enforce atomicity: writing a single parent log into a `journal_entries` table must trigger a minimum of two matching line logs inside a `journal_lines` table.
* The relational sum of amounts mapped across single `journal_entry_id` line arrays must precisely balance to `0` (positive allocations map to Debits, negative values map to Credits). Hold data scale lengths securely at `NUMERIC(15, 2)`.

---

## 2. Mandatory Functional Implementations to Generate

### A. Python FastAPI Endpoint (`/api/v1/transactions/sms-sync`)
* Accept incoming JSON schemas containing `sender`, `body`, `timestamp`, and `sim_slot`.
* Execute filtering to ignore non-financial texts instantly with a `422 Unprocessable Entity` status code.
* Use regex definitions to securely unpack the text body, extract the numerical value, flag the transaction direction (Debit/Credit), map account markers, and clean merchant handles.

### B. Python Dual-Regime Indian Income Tax Optimizer
* Code a clean mathematical computation class accepting income structures (`basic_pay`, `hra_received`, `special_allowance`) and credit records (`80C`, `80D`).
* Implement full parameter isolation for HRA thresholds under metro vs. non-metro boundaries.
* Compare computed liabilities across the traditional Old Regime rules against updated New Regime structural slabs, accounting for respective standard deductions and Section 87A rebate rules. Output a recommendation string highlighting net monthly cash increases.

### C. Container Infrastructure Topology
* Output a `docker-compose.yml` file coordinating an API gateway, a background Celery daemon worker, a persistent storage PostgreSQL service with embedded system health checks, and a Redis broker instance.
