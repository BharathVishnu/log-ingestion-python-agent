import argparse
from regex_engine import match_log
from llm_engine import llm_parse
from regex_builder import build_regex
from rule_store import save_rule
from util import save_output

def process_log(log):

    parsed = match_log(log)

    if parsed:
        print("Regex matched")
        return parsed

    print("Using LLM...")
    parsed = llm_parse(log)

    if not parsed:
        return {"event": "unknown"}

    regex = build_regex(log, parsed)

    rule = {
        "regex": regex,
        "fields": list(parsed.keys())
    }

    save_rule(rule)

    save_output(log,parsed)

    print("Learned new pattern")

    return parsed



