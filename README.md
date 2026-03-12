Configurable Workflow Decision Platform
Overview

This project implements a Configurable Workflow Decision Platform capable of processing incoming requests, evaluating rules, executing workflow stages, maintaining state, recording audit logs, and handling failures with retries.

The system is designed to simulate real-world business workflows such as:

Application approval workflows

Claim processing workflows

Vendor approval workflows

Document verification workflows

The platform is configurable and resilient, allowing workflows and rules to be modified without major code changes.

Key Features

REST API interface built using FastAPI

Configurable workflows defined via JSON configuration

Rule-based decision engine for evaluating business rules

Workflow execution engine for step-by-step processing

External dependency simulation to test resilience

Retry mechanism for handling dependency failures

Audit logging system for explainable decision tracking

State management service for workflow lifecycle tracking

Idempotency handling to prevent duplicate request processing

Automated test coverage using pytest

System Architecture

The system follows a modular architecture where each component handles a specific responsibility.

Client Request
      ↓
FastAPI REST API
      ↓
Request Validation (Pydantic)
      ↓
Workflow Engine
      ↓
Rule Engine
      ↓
External Dependency (Mock API)
      ↓
State Management Service
      ↓
Audit Logging Service

This architecture ensures low coupling and high configurability.

Project Structure
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
Installation and Setup
1. Clone the repository
git clone <your-repo-url>
cd decision-system
2. Install dependencies
pip install -r requirements.txt
3. Run the API server
uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs
API Usage
Process Workflow Request

Endpoint:

POST /process-request

Example request:

{
  "request_id": "REQ20",
  "workflow": "loan_approval",
  "income": 50000,
  "credit_score": 700
}

Example response:

{
  "request_id": "REQ20",
  "status": "approved",
  "history": [
    {
      "step": "validate_input",
      "result": "validated"
    },
    {
      "step": "fetch_credit_score",
      "result": 738
    },
    {
      "step": "evaluate_rules",
      "result": {
        "decision": "approve",
        "trace": [
          "minimum_income",
          "credit_score_check"
        ]
      }
    }
  ]
}
Audit Logs

Endpoint:

GET /audit-logs

Returns workflow execution logs and rule decisions for transparency.

Example response:

[
  {
    "request_id": "REQ20",
    "step": "evaluate_rules",
    "details": {
      "decision": "approve",
      "rules_triggered": [
        "minimum_income",
        "credit_score_check"
      ]
    },
    "timestamp": "2026-03-12T10:45:21"
  }
]
Configuration Model

The system is driven by configuration files.

workflows.json

Defines workflow steps:

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
rules.json

Defines rule conditions and actions:

{
  "name": "credit_score_check",
  "condition": "credit_score >= 650",
  "action": "approve"
}

This approach allows workflows and rules to change without modifying code.

Testing

Automated tests are implemented using pytest.

Run tests:

python -m pytest

Test coverage includes:

rule evaluation

workflow execution

dependency failure

retry logic

duplicate request handling

Failure Handling

The system simulates external API failures.

Retry strategy:

Max retries = 3

If all retries fail, the workflow returns:

status = retry

This demonstrates system resilience.

Future Improvements

Possible enhancements include:

persistent database storage (PostgreSQL)

message queue for workflow orchestration

distributed microservices architecture

advanced rule engine with rule DSL

containerized deployment using Docker

Conclusion

This project demonstrates a resilient and configurable workflow decision platform capable of handling real-world business workflows with rule-based evaluation, auditability, and failure handling.

The modular architecture ensures the system is maintainable, extensible, and suitable for scaling in production environments.