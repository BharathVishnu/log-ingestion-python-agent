import re
from rule_store import load_rules

def match_log(log):

    for rule in load_rules():

        try:
            match = re.search(rule["regex"], log)
        except:
            continue

        if match:
            data = {}

            for i, field in enumerate(rule["fields"]):
                try:
                    data[field] = match.group(i + 1)
                except:
                    data[field] = None

            return data

    return None
