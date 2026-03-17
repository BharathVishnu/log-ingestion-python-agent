import argparse
from regex_engine import match_log
from llm_engine import llm_parse
from regex_builder import build_regex
from rule_store import save_rule
from util import save_output
from vector_store.store import search_similar, add_to_store
import re
from regex_engine import match_log

def process_log(log):

    similar = search_similar(log)

    if similar:
        print("RAG matched")

        match = re.search(similar["regex"], log)

        if match:
            data = {}

            for i, field in enumerate(similar["parsed"].keys()):
                try:
                    data[field] = match.group(i + 1)
                except:
                    data[field] = None

            return data

    parsed = match_log(log)

    if parsed:
        print("Regex matched")
        return parsed

    print("Using LLM...")
    parsed = llm_parse(log)

    if not parsed:
        parsed = {"event": "unknown"}

    
    regex = build_regex(log, parsed)

    rule = {
        "regex": regex,
        "fields": list(parsed.keys())
    }


    add_to_store(log, parsed, regex)
    save_output(log,parsed)

    print("     Learned + stored in RAG")

    return parsed