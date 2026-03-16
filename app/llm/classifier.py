import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT = """
Classify this log into one category:

normal
suspicious
security_incident

Return only the category.
"""

def classify_log(log):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model":"llama3",
            "prompt":PROMPT + log,
            "stream":False
        }
    )

    return response.json()["response"].strip()