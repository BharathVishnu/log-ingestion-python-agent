import re

def detect_type(value):

    value = str(value)

    if re.match(r"\d+\.\d+\.\d+\.\d+", value):
        return r"([0-9.]+)"

    elif re.match(r"\d+$", value):
        return r"(\d+)"

    elif re.match(r"[a-zA-Z_]+$", value):
        return r"(\w+)"

    elif "@" in value:
        return r"([\w\.-]+@[\w\.-]+)"

    return r"(.+?)"


def build_regex(log, parsed):

    pattern = log

    for value in parsed.values():

        if not value:
            continue

        pattern = pattern.replace(
            str(value),
            detect_type(value),
            1
        )

    return pattern
