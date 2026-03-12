from pydantic import BaseModel

class LoanRequest(BaseModel):
    income: int
    credit_score: int