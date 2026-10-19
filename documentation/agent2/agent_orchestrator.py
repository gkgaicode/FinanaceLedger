#!/usr/bin/env python3
"""
Generalized Business Use-Case Agent Orchestrator (agent_orchestrator.py)

Dynamically scaffolds a complete, production-ready full-stack monorepo project
structure for ANY supplied business use case by chaining 6 specialized domain skills:
  1. observability_cicd_skill-> PII-Sanitized Logger (logger.py), Unit/Integration Tests, & GitHub Actions CI/CD
  2. domain_core_skill       -> PostgreSQL 15 double-entry schema + Domain/Tax Optimization Engine
  3. ingestion_api_skill     -> FastAPI gateway (CORS + logging middleware), Regex parser, Celery/Redis worker
  4. client_ui_skill         -> React 18 + TypeScript + Vite + Tailwind CSS Web UI & Flutter Mobile Client
  5. infra_devops_skill      -> Multi-stage non-root Dockerfile, Docker Compose, Nginx proxy, & install scripts
  6. docs_knowledge_skill    -> README.md, KNOWLEDGE_BASE.md, AGENT_INSTRUCTIONS.md, and init_docs.sh
"""
import argparse
import json
import os
import re
import subprocess
import sys
from importlib import import_module
from typing import Dict, Any

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)


PRESET_USE_CASES: Dict[str, Dict[str, Any]] = {
    "fintech-personal-ledger": {
        "project_slug": "indian-salaried-fintech-ledger",
        "project_title": "Indian Salaried Personal Finance Core Ledger Engine",
        "domain_name": "Personal Finance, Account Aggregator & Tax Accounting (India)",
        "target_persona": "Salaried Professionals in India",
        "currency_or_unit": "INR",
        "regulatory_framework": "RBI Account Aggregator (ReBIT) & CERT-In FinTech Security Standards",
        "account_or_entity_categories": ["ASSET", "LIABILITY", "INCOME", "EXPENSE"],
        "feature_mappings": [
            {
                "source_feature": "Bank Feeds & Categorization",
                "target_equivalent": "Multi-Account Aggregation (Sahamati AA & SMS)",
                "use_case_description": "Sync salary accounts, credit cards, and wallets; auto-tag food, utilities, and EMIs.",
            },
            {
                "source_feature": "Invoicing & Accounts Receivable",
                "target_equivalent": "Salary & Corporate Reimbursement Claims",
                "use_case_description": "Track monthly payroll credits, fuel/medical reimbursement claims, and peer split-settlements.",
            },
            {
                "source_feature": "Expense Tracking & Receipt Capture",
                "target_equivalent": "Tax-Deductible Proof Vault",
                "use_case_description": "Scan receipts for medical allowances, LTA, rent, and Section 80C/80D/HRA exemptions.",
            },
            {
                "source_feature": "Bills & Accounts Payable",
                "target_equivalent": "Fixed Obligations & EMI Calendar",
                "use_case_description": "Track utility bills, subscriptions, credit card due dates, and home/auto loan amortization.",
            },
            {
                "source_feature": "P&L & Balance Sheet",
                "target_equivalent": "Net Savings & Net Worth Statements",
                "use_case_description": "Income minus living expenses yields net savings; total assets minus debt yields real-time net worth.",
            },
            {
                "source_feature": "Sales Tax / VAT / GST Filing",
                "target_equivalent": "Dual-Regime Income Tax (ITR) Optimizer",
                "use_case_description": "Reconcile TDS from payslips and compare Old vs. New Tax Regime to maximize monthly take-home pay.",
            },
        ],
        "ingestion_spec": {
            "channel_name": "On-Device Android Banking SMS & ReBIT Account Aggregator Webhook",
            "valid_keywords": ["DEBITED", "CREDITED", "SPENT", "CHARGED", "SUCCESSFULLY PAID"],
            "outflow_keywords": ["DEBITED", "SPENT", "PAID", "CHARGED"],
            "value_regex": r"(?:RS|INR|RS\.)\s*([\d,]+\.?\d*)",
            "source_id_regex": r"(?:A/C|A\s*/\s*C|CARD|ACC)\s*(?:ENDING|XX|X)*\s*(\d{3,4})",
            "counterparty_regex": r"(?:TO|INFO|VPA|AT)\s+([A-Z0-9\s\.\-\_\@\/]+?)(?:\s+ON|\s+BALANCE|\s+LINKED|$)",
            "sample_payload_text": "Your A/c XX4321 has been Debited for Rs. 1,250.50 via UPI to SWIGGY@HDFCBANK on 19-10-2026.",
            "sample_sender": "AD-HDFCBK",
        },
        "optimization_spec": {
            "engine_class_name": "TaxOptimizationEngine",
            "strategy_a_name": "OLD_REGIME",
            "strategy_b_name": "NEW_REGIME",
            "description": "Compares Indian Income Tax Old Regime (HRA, 80C, 80D, 50k Standard Deduction) against New Regime (75k Standard Deduction, updated slabs) with 4% Cess.",
            "strategy_a_base_deduction": 50000.0,
            "strategy_b_base_deduction": 75000.0,
            "sample_base_value": 500000.0,
            "sample_secondary_value": 200000.0,
            "sample_allowance_value": 500000.0,
        },
    },
    "ecommerce-inventory-hub": {
        "project_slug": "ecommerce-inventory-order-hub",
        "project_title": "Omnichannel E-Commerce Inventory & Order Ledger Engine",
        "domain_name": "Retail Supply Chain, Inventory Accounting & Order Fulfillment",
        "target_persona": "D2C Merchants & Warehouse Operations Teams",
        "currency_or_unit": "USD",
        "regulatory_framework": "SOC2 Type II & PCI-DSS E-Commerce Compliance",
        "account_or_entity_categories": ["INVENTORY_ASSET", "PAYABLE_LIABILITY", "REVENUE", "COGS_EXPENSE"],
        "feature_mappings": [
            {
                "source_feature": "Multi-Channel Order Sync",
                "target_equivalent": "Unified Webhook & Carrier Telemetry Ingestion",
                "use_case_description": "Ingest real-time storefront orders, warehouse scans, and carrier dispatch events.",
            },
            {
                "source_feature": "Double-Entry Stock & COGS Ledger",
                "target_equivalent": "Atomic SKU Balance & Cost of Goods Sold Splits",
                "use_case_description": "Ensure every order fulfillment debits COGS/Receivables and credits Inventory Asset seamlessly.",
            },
            {
                "source_feature": "Fulfillment Routing & Margin Optimizer",
                "target_equivalent": "3PL vs. In-House Fulfillment Cost Comparator",
                "use_case_description": "Evaluate storage, pick-pack fees, and shipping zones to choose the highest-margin fulfillment track.",
            },
        ],
        "ingestion_spec": {
            "channel_name": "Storefront Order & Carrier Scan Telemetry Stream",
            "valid_keywords": ["DEBITED", "CREDITED", "DISPATCHED", "RECEIVED", "CHARGED", "PAID"],
            "outflow_keywords": ["DEBITED", "DISPATCHED", "CHARGED", "PAID"],
            "value_regex": r"(?:USD|\$|RS|INR|AMT)\s*([\d,]+\.?\d*)",
            "source_id_regex": r"(?:WH|NODE|ACC|A/C)\s*(?:ENDING|XX|X|#)*\s*(\d{3,4})",
            "counterparty_regex": r"(?:TO|VIA|CARRIER|AT)\s+([A-Z0-9\s\.\-\_\@\/]+?)(?:\s+ON|\s+STATUS|$)",
            "sample_payload_text": "Warehouse WH #4321 has been Debited for USD 1,250.50 via CARRIER to FEDEX@LOGISTICS on 19-10-2026.",
            "sample_sender": "SHOPIFY-WMS",
        },
        "optimization_spec": {
            "engine_class_name": "FulfillmentMarginOptimizer",
            "strategy_a_name": "DEDICATED_WAREHOUSE",
            "strategy_b_name": "DISTRIBUTED_3PL",
            "description": "Compares dedicated warehouse fixed lease/labor credits against distributed 3PL slab pricing.",
            "strategy_a_base_deduction": 50000.0,
            "strategy_b_base_deduction": 75000.0,
            "sample_base_value": 500000.0,
            "sample_secondary_value": 200000.0,
            "sample_allowance_value": 500000.0,
        },
    },
}


def build_dynamic_spec_from_args(args: argparse.Namespace) -> Dict[str, Any]:
    if args.config:
        with open(args.config, "r", encoding="utf-8") as f:
            return json.load(f)

    if args.preset and args.preset in PRESET_USE_CASES and not args.use_case:
        return PRESET_USE_CASES[args.preset]

    use_case_title = args.use_case or "Indian Salaried Personal Finance Core Ledger Engine"
    slug = re.sub(r"[^a-z0-9]+", "-", use_case_title.lower()).strip("-")[:48] or "custom-domain-platform"
    domain = args.domain or f"{use_case_title} Domain"
    persona = args.persona or "Enterprise & Consumer End Users"
    currency = args.currency or "INR"

    base = json.loads(json.dumps(PRESET_USE_CASES["fintech-personal-ledger"]))
    base["project_slug"] = slug
    base["project_title"] = use_case_title
    base["domain_name"] = domain
    base["target_persona"] = persona
    base["currency_or_unit"] = currency

    if args.use_case:
        base["feature_mappings"] = [
            {
                "source_feature": "Core Event Capture & Ingestion",
                "target_equivalent": f"{use_case_title} Real-Time Telemetry Gateway",
                "use_case_description": f"Ingests, validates, and normalizes inbound operational events for {persona}.",
            },
            {
                "source_feature": "Double-Entry Accounting & Audit Trail",
                "target_equivalent": "ACID Relational Split Ledger",
                "use_case_description": f"Tracks every {currency} movement across asset, liability, income, and expense buckets with zero discrepancy.",
            },
            {
                "source_feature": "Rule & Cost Optimization Engine",
                "target_equivalent": "Dual-Track Strategy Comparator",
                "use_case_description": f"Evaluates itemized vs. slab-based operational rules in {domain} to maximize net savings.",
            },
            {
                "source_feature": "Omnichannel Client Interfaces",
                "target_equivalent": "React Web Console & Flutter Mobile Sync Client",
                "use_case_description": f"Provides interactive SVG analytics and background mobile synchronization for {persona}.",
            },
        ]
    return base


class BusinessProjectAgentOrchestrator:
    """Master Agent Orchestrator that chains 6 modular domain skills to generate a complete monorepo."""

    SKILL_PIPELINE = [
        "observability_cicd_skill",
        "domain_core_skill",
        "ingestion_api_skill",
        "client_ui_skill",
        "infra_devops_skill",
        "docs_knowledge_skill",
    ]

    def __init__(self, output_dir: str, spec: Dict[str, Any]):
        self.output_dir = os.path.abspath(output_dir)
        self.spec = spec

    def bootstrap_workspace(self) -> None:
        print(f"[Agent Orchestrator] Scaffolding monorepo directories inside: {self.output_dir}")
        folders = [
            "infrastructure",
            "backend",
            "web/src",
            "mobile/lib",
            "documentation",
            "scripts",
            ".github/workflows",
        ]
        for folder in folders:
            os.makedirs(os.path.join(self.output_dir, folder), exist_ok=True)

        spec_path = os.path.join(self.output_dir, "documentation", "use_case_spec.json")
        with open(spec_path, "w", encoding="utf-8") as f:
            json.dump(self.spec, f, indent=2)

    def execute_agent_pipeline(self) -> None:
        self.bootstrap_workspace()
        for skill_name in self.SKILL_PIPELINE:
            print(f"[Agent Orchestrator] Executing skill module: {skill_name}")
            skill_module = import_module(f"skills.{skill_name}")
            skill_module.generate_domain_artifacts(self.output_dir, self.spec)

        print(f"[Agent Sign-off] Project '{self.spec['project_title']}' successfully generated at {self.output_dir}")

    def verify_generated_project(self) -> bool:
        print("[Agent Verification] Compiling Python modules and running unit test suites...")
        backend_dir = os.path.join(self.output_dir, "backend")
        py_files = [
            "logger.py",
            "parser.py",
            "domain_engine.py",
            "tax_engine.py",
            "tasks.py",
            "main.py",
            "test_unit.py",
            "test_integration.py",
        ]
        for py_file in py_files:
            full_path = os.path.join(backend_dir, py_file)
            subprocess.run([sys.executable, "-m", "py_compile", full_path], check=True)

        subprocess.run([sys.executable, os.path.join(backend_dir, "parser.py")], cwd=backend_dir, check=True)
        subprocess.run([sys.executable, os.path.join(backend_dir, "domain_engine.py")], cwd=backend_dir, check=True)
        subprocess.run(
            [sys.executable, "-m", "unittest", "test_unit.py", "-v"],
            cwd=backend_dir,
            check=True,
        )
        print("[Agent Verification] All compilation and unit test assertions passed!")
        return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a full-stack monorepo for any supplied business use case.")
    parser.add_argument("--use-case", type=str, help="Title or summary of the business use case.")
    parser.add_argument("--domain", type=str, help="Business domain description.")
    parser.add_argument("--persona", type=str, help="Target end-user persona.")
    parser.add_argument("--currency", type=str, default="INR", help="Primary currency or unit code (e.g. INR, USD).")
    parser.add_argument(
        "--preset",
        type=str,
        choices=list(PRESET_USE_CASES.keys()),
        default="fintech-personal-ledger",
        help="Built-in preset use case.",
    )
    parser.add_argument("--config", type=str, help="Path to a custom JSON business use-case specification file.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./generated_project",
        help="Target directory where the monorepo will be generated.",
    )
    parser.add_argument("--verify", action="store_true", help="Compile and run unit tests on generated backend modules.")

    args = parser.parse_args()
    spec = build_dynamic_spec_from_args(args)
    orchestrator = BusinessProjectAgentOrchestrator(output_dir=args.output_dir, spec=spec)
    orchestrator.execute_agent_pipeline()
    if args.verify:
        orchestrator.verify_generated_project()


if __name__ == "__main__":
    main()
