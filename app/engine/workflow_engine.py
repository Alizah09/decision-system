import json
from app.engine.rule_engine import RuleEngine
from app.external.credit_api_mock import fetch_credit_score
from app.services.audit_service import AuditService

class WorkflowEngine:

    def __init__(self):
        self.audit_service = AuditService()
        with open("app/config/workflows.json") as f:
            self.workflows = json.load(f)

        self.rule_engine = RuleEngine("app/config/rules.json")

    def execute(self, workflow_name, request_data, state_service):

        workflow = self.workflows[workflow_name]["steps"]

        request_id = request_data["request_id"]

        for step in workflow:

            try:

                if step == "validate_input":
                    state_service.update_state(request_id, step, "validated")
                    self.audit_service.log_event(request_id, step, {"status": "input validated"})
                    
                elif step == "fetch_credit_score":
                    max_retries = 3
                    attempt = 0
                    while attempt < max_retries:
                        try:
                            score = fetch_credit_score()
                            request_data["credit_score"] = score
                            state_service.update_state(request_id, step, score)
                            self.audit_service.log_event(request_id, step, {"credit_score": score, "attempt": attempt + 1})
                            break
                        except Exception as e:
                            attempt += 1
                            self.audit_service.log_event(request_id,step,{"error": str(e), "attempt": attempt})
                            if attempt == max_retries:
                                state_service.update_state(request_id, step, "dependency_failed")
                                return "retry"

                elif step == "evaluate_rules":
                    result = self.rule_engine.evaluate(request_data)
                    state_service.update_state(request_id, step, result)

                    decision = result["decision"]

                    if decision == "approve":
                        return "approved"

                    elif decision == "manual_review":
                        return "manual_review"

                    elif decision == "reject":
                        return "rejected"

                elif step == "final_decision":
                    state_service.update_state(request_id, step, "completed")

            except Exception as e:

                state_service.update_state(request_id, step, "failed")

                return "retry"

        return "completed"