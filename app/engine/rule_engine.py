import json


class RuleEngine:

    def __init__(self, rule_file):
        with open(rule_file, "r") as f:
            self.rules = json.load(f)["rules"]

    def evaluate(self, data):
        decision_trace = []
        final_action = None

        for rule in self.rules:
            condition = rule["condition"]

            if eval(condition, {}, data):
                decision_trace.append(rule["name"])
                final_action = rule["action"]

                if final_action in ["approve", "reject", "manual_review"]:
                    break

        return {
            "decision": final_action,
            "trace": decision_trace
        }