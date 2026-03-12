# ⚙️ Configurable Workflow Decision Platform

---

## 📖 Project Overview

This project implements a **Configurable Workflow Decision Platform** capable of processing incoming requests, evaluating rules, executing workflow stages, maintaining state, recording audit logs, and handling failures with retries.

The system simulates real-world business workflows such as:

- Application approval workflow
- Claim processing workflow
- Vendor approval workflow
- Document verification workflow

The platform is **configurable, resilient, and auditable**, allowing workflows and rules to change without modifying core application logic.

---

## 🏗 System Architecture
```
flowchart TD
    A[Client Request] --> B[FastAPI REST API]
    B --> C[Request Validation (Pydantic)]
    C --> D[Workflow Engine]
    D --> E[Rule Engine]
    E --> F[External Dependency\n(Mock API)]
    F --> G[State Management Service]
    G --> H[Audit Logging Service]
```
## Project Structure
```
decision-system/
│
├── app/
│   ├── engine/
│   │   ├── workflow_engine.py
│   │   └── rule_engine.py
│   │
│   ├── services/
│   │   ├── state_service.py
│   │   └── audit_service.py
│   │
│   ├── models/
│   │   └── request_model.py
│   │
│   ├── config/
│   │   ├── workflows.json
│   │   └── rules.json
│   │
│   ├── external/
│   │   └── credit_api_mock.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_rules.py
│   └── test_workflow.py
│
├── architecture.md
├── README.md
└── requirements.txt
```
## 🚀 API Endpoints
Process Workflow Request
POST /process-request
Example Request
```
{
  "request_id": "REQ20",
  "workflow": "loan_approval",
  "income": 50000,
  "credit_score": 700
}
```
Example Response

```

{
  "request_id": "REQ20",
  "status": "approved"
}
Get Audit Logs
GET /audit-logs
```
Example Response
```
[
  {
    "request_id": "REQ20",
    "step": "evaluate_rules",
    "decision": "approve",
    "rules_triggered": [
      "minimum_income",
      "credit_score_check"
    ]
  }
]
```
### 🔁 Failure Handling & Retry Strategy

External dependency failures are handled with retry logic.

Max Retries = 3

If all retries fail:

Workflow Status → retry

Failures are recorded in the audit logs.

### 🔄 Idempotency Handling

To prevent duplicate processing:

If request_id exists → return existing result
Else → execute workflow

This ensures consistent results for repeated requests.

## ⚙️ Configuration Model

The platform is driven by configuration files.

config/workflows.json
config/rules.json

Example Workflow Configuration
```
{
  "loan_approval": {
    "steps": [
      "validate_input",
      "fetch_credit_score",
      "evaluate_rules",
      "final_decision"
    ]
  }
}
```
## 🧪 Testing

Run tests using pytest:

python -m pytest

Test coverage includes:

Workflow execution

Rule evaluation

Duplicate request handling

Retry logic

Dependency failure simulation

## 🧰 Tech Stack

Python

FastAPI

Pydantic

Pytest

JSON Configuration

## Git & GitHub

📌 Repository
https://github.com/Alizah09/decision-system
## 🎯 Conclusion

This project demonstrates a resilient and configurable workflow decision platform capable of handling rule-based business workflows with auditability, retry logic, and modular architecture.
