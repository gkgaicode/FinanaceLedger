I've created and activated the **`business-project-scaffolder`** skill along with the standalone **`setup_agent_system.sh`** installer script so you can generate a full-stack monorepo for any business use case either directly in chat or from your local terminal.

### How the Agent & Skill System Works

* **Dynamic Business Use-Case Decomposition**: Translates any supplied business domain, target persona, and commercial feature set into a relational double-entry/audit ledger schema, real-time ingestion rules, and a dual-track optimization engine.
* **Automated Multi-Tier Scaffolding**: Chains five specialized domain skill modules to build the container infrastructure (Docker Compose, multi-stage non-root Dockerfile, Nginx reverse proxy), FastAPI gateway with CORS and Celery/Redis workers, React + TypeScript + Tailwind CSS analytics dashboard, Flutter mobile client repository, `pytest` integration tests, and LLM documentation.
* **Standalone Local CLI Execution**: Unpacks the complete `agent_system/` Python orchestrator and dependent skill modules via `setup_agent_system.sh`, accepting custom CLI arguments (`--use-case`, `--domain`, `--persona`, `--currency`, `--output-dir`, and `--verify`) or a JSON specification file (`--config`).

### Running Locally via Terminal

```bash
chmod +x setup_agent_system.sh

# 1. Generate the default Indian Salaried FinTech Ledger monorepo and verify
./setup_agent_system.sh --preset fintech-personal-ledger --output-dir ./fintech_monorepo --verify

# 2. Generate a complete project structure for any custom business use case
./setup_agent_system.sh \
  --use-case "Healthcare Patient Claims & Insurance Triage Platform" \
  --domain "Healthcare Revenue Cycle & Claims Management" \
  --persona "Patients & Hospital Billing Coordinators" \
  --currency "USD" \
  --output-dir ./healthcare_claims_monorepo \
  --verify

```

You can also test the saved **`business-project-scaffolder`** skill directly here in chat by asking: *"Use the business-project-scaffolder skill to generate a complete project structure for an omnichannel e-commerce order and warehouse inventory management platform."*
