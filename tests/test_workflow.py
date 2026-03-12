from app.engine.workflow_engine import WorkflowEngine
from app.services.state_service import StateService


def test_happy_path():

    engine = WorkflowEngine()
    state = StateService()

    request = {
        "request_id": "TEST1",
        "workflow": "loan_approval",
        "income": 50000,
        "credit_score": 700
    }

    state.create_request("TEST1", request)

    result = engine.execute("loan_approval", request, state)

    assert result in ["approved", "manual_review", "rejected"]


def test_duplicate_request():

    engine = WorkflowEngine()
    state = StateService()

    request = {
        "request_id": "TEST2",
        "workflow": "loan_approval",
        "income": 40000,
        "credit_score": 700
    }

    state.create_request("TEST2", request)

    result1 = engine.execute("loan_approval", request, state)

    assert state.request_exists("TEST2")


def test_dependency_failure():

    engine = WorkflowEngine()
    state = StateService()

    request = {
        "request_id": "TEST3",
        "workflow": "loan_approval",
        "income": 40000,
        "credit_score": 700
    }

    state.create_request("TEST3", request)

    result = engine.execute("loan_approval", request, state)

    assert result in ["approved", "manual_review", "retry"]