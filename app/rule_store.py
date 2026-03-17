import json

FILE = "rules.json"

def load_rules():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return []

def save_rule(rule):

    rules = load_rules()

    for r in rules:
        if r["regex"] == rule["regex"]:
            return

    rules.insert(0, rule)

    with open(FILE, "w") as f:
        json.dump(rules, f, indent=2)
