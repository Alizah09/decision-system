from app.engine.rule_engine import RuleEngine

def test_rule_engine():

    engine = RuleEngine("app/config/rules.json")

    result = engine.evaluate(60000, 750)

    assert result == "Approved"