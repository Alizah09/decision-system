from app.engine.rule_engine import RuleEngine

engine = RuleEngine("app/config/rules.json")

income = 45000
credit_score = 650

decision = engine.evaluate(income, credit_score)

print("Decision:", decision)