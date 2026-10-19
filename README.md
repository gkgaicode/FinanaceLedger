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
