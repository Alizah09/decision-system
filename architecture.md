# Configurable Workflow Decision Platform
## 1. System Overview

This project implements a configurable workflow decision system capable of processing incoming requests, evaluating rules, executing workflow stages, maintaining state, and recording audit logs.

The platform is designed to support multiple business workflows such as:

Loan approval

Vendor onboarding

Claim processing

Document verification

The system is designed to be configurable, resilient, and auditable, allowing workflows and rules to change without modifying the core application logic.

## 2. System Architecture

The system follows a modular service-oriented architecture.
```
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
```
Each component has a clear responsibility, enabling maintainability and extensibility.

## 3. Key Components
### 3.1 API Layer (FastAPI)

The API layer provides a REST interface for interacting with the system.

Endpoints implemented:

POST /process-request
GET  /audit-logs

Responsibilities:

Receive incoming requests

Validate input schema

Trigger workflow execution

Return decision responses

FastAPI was selected because it provides:

automatic validation

OpenAPI documentation

high performance

### 3.2 Workflow Engine

The Workflow Engine orchestrates the execution of workflow steps defined in configuration.

Responsibilities:

load workflow configuration

execute workflow steps sequentially

integrate rule engine

manage retry logic

handle failures

Example workflow configuration:
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
This design ensures workflows can change without modifying application code.

### 3.3 Rule Engine

The Rule Engine evaluates business rules against incoming request data.

Example rule configuration:
```
{
  "name": "credit_score_check",
  "condition": "credit_score >= 650",
  "action": "approve"
}
```
Responsibilities:

evaluate rule conditions

trigger decisions

produce rule trace logs

This enables explainable decision making.

### 3.4 State Management Service

The state service stores the lifecycle of workflow requests.

Each request contains:

request_id
status
data
execution history

Example state record:
```
{
  request_id: REQ20
  status: approved
  history: [...]
}
```
State management enables:

workflow tracking

duplicate request detection

idempotency

### 3.5 Audit Logging Service

The audit service records all workflow actions and rule evaluations.

Example audit log entry:
```
{
  request_id: REQ20
  step: evaluate_rules
  decision: approve
  rules_triggered: [...]
  timestamp: ...
}
```
This provides:

traceability

explainable decisions

debugging capability

### 3.6 External Dependency Simulation

The system simulates an external service:

Credit Score API

This dependency intentionally fails randomly to test resilience.

Example simulation:

30% chance of failure
70% chance of success

This demonstrates system robustness under real-world conditions.

## 4. Failure Handling and Retry Strategy

External dependency calls are wrapped in retry logic.

Retry strategy:

Max retries = 3

If all retries fail:

workflow status → retry

Failures are recorded in audit logs for observability.

## 5. Idempotency Handling

To prevent duplicate processing, the system checks if a request ID already exists.

If a duplicate request is received:

Return existing result
Do not re-execute workflow

This ensures consistent behavior under repeated submissions.

## 6. Configuration Model

The system is driven by configuration files:

config/workflows.json
config/rules.json

Benefits:

workflows configurable

rule updates without code changes

improved maintainability

## 7. Testing Strategy

Automated tests were implemented using pytest.

Test coverage includes:

workflow execution

rule evaluation

invalid input handling

duplicate request detection

dependency failure

retry logic

This ensures reliability of system components.

## 8. Scalability Considerations

For production environments the system could scale using:

stateless API servers

distributed workflow queues

persistent database for state storage

centralized logging system

containerized deployment

This allows the system to handle high volumes of requests.

## 9. Design Trade-offs
In-memory state storage

Pros:

simple implementation

faster development

Cons:

not persistent across restarts

Future improvement:

Use PostgreSQL or Redis
Rule evaluation using Python expressions

Pros:

flexible rule definitions

easy configuration

Cons:

requires careful validation

Future improvement:

dedicated rule DSL
## 10. Conclusion

The implemented system provides a flexible and resilient workflow decision platform capable of handling configurable business processes.

Key capabilities achieved:

configurable workflows

rule-based decision making

auditability

failure handling

idempotency

API-based access

automated testing

The modular architecture enables the system to evolve into a production-grade workflow orchestration platform.
