import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT = """
You are a cybersecurity log normalization engine.

Convert logs into JSON using this schema:

{
 "timestamp":"",
 "log_source":"",
 "event_type":"",
 "severity":"",
 "username":"",
 "source_ip":"",
 "destination_ip":"",
 "port":"",
 "protocol":"",
 "service":"",
 "status":"",
 "message":"",
 "raw_log":""
}

Return only JSON.
"""

def normalize_log(log):

    prompt = PROMPT + "\nLog:\n" + log

    response = requests.post(
        OLLAMA_URL,
        json={
            "model":"llama3",
            "prompt":prompt,
            "stream":False
        }
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except:
        return {"raw_log":log}