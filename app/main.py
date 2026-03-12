from fastapi import FastAPI
from app.models.request_model import WorkflowRequest
from app.engine.workflow_engine import WorkflowEngine
from app.services.state_service import StateService

app = FastAPI()

workflow_engine = WorkflowEngine()
state_service = StateService()

@app.get("/audit-logs")
def get_audit_logs():
    return workflow_engine.audit_service.get_logs()

@app.post("/process-request")
def process_request(request: WorkflowRequest):

    request_data = request.dict()
    request_id = request_data["request_id"]

    # idempotency check
    if state_service.request_exists(request_id):
        return {
            "message": "Duplicate request",
            "existing_result": state_service.get_request(request_id)
        }

    state_service.create_request(request_id, request_data)

    result = workflow_engine.execute(
        request_data["workflow"],
        request_data,
        state_service
    )

    return {
        "request_id": request_id,
        "status": result,
        "history": state_service.get_request(request_id)["history"]
    }