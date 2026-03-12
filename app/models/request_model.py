from pydantic import BaseModel


class WorkflowRequest(BaseModel):
    request_id: str
    workflow: str
    income: int
    credit_score: int