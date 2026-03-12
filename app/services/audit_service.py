from datetime import datetime


class AuditService:

    def __init__(self):
        self.logs = []

    def log_event(self, request_id, step, details):

        log_entry = {
            "request_id": request_id,
            "step": step,
            "details": details,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.logs.append(log_entry)

    def get_logs(self):
        return self.logs