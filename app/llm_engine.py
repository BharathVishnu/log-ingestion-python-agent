import requests
import json

def llm_parse(log):

    prompt = f"""
Extract structured fields from this log.

Log:
{log}

Return JSON only.
"""

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )

        text = res.json()["response"]

        start = text.find("{")
        end = text.rfind("}") + 1

        if start == -1:
            return None

        return json.loads(text[start:end])

    except:
        return None
