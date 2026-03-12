from app.engine.rule_engine import RuleEngine


def test_rule_engine():
    engine = RuleEngine("app/config/rules.json")

    data = {
        "income": 40000,
        "credit_score": 700
    }

    result = engine.evaluate(data)

    assert result["decision"] == "approve"