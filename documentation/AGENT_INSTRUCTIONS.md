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
* Craft a multi-stage execution `Dockerfile` utilizing a `builder` phase to isolate wheel compilation artifacts, and a `runner` stage executing as an unprivileged, custom non-root system application user (`fintechuser`).

### D. Flutter Interface Communication Classes
* Generate Dart models containing comprehensive `toJson()` serialization capabilities matching the backend ingest format.
* Build a clean network connectivity repository managing custom timeout tolerances, processing HTTP header token authorization parameters, and logging background retries for network drops.

---

## 3. Generation Prompt Prompt Template
*When you prompt a downstream LLM or Agent tool, copy-paste the template below alongside these instruction files:*

> "Using the specifications provided inside KNOWLEDGE_BASE.md and AGENT_INSTRUCTIONS.md, generate the complete code files for an Indian Salaried Personal Finance Engine. Ensure the Python files include standard library regex imports, strict Pydantic model configurations, and precise mathematical operations. Ensure the Dart components feature comprehensive typing structures and error-handling try-catch blocks. Do not use placeholder code comments; output fully typed, deployment-ready scripts."
