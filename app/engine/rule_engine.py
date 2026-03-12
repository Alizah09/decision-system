import json

class RuleEngine:

    def __init__(self, rule_file):
        with open(rule_file, "r") as f:
            self.rules = json.load(f)["rules"]

    def evaluate(self, income, credit_score):

        for rule in self.rules:
            cond = rule["conditions"]

            if income >= cond["income"] and credit_score >= cond["credit_score"]:
                return rule["decision"]

        return "Rejected"