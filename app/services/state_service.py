class StateService:

    def __init__(self):
        self.store = {}

    def create_request(self, request_id, data):
        self.store[request_id] = {
            "status": "processing",
            "data": data,
            "history": []
        }

    def update_state(self, request_id, step, result):
        self.store[request_id]["history"].append({
            "step": step,
            "result": result
        })

    def get_request(self, request_id):
        return self.store.get(request_id)
    
    def request_exists(self, request_id):
        return request_id in self.store