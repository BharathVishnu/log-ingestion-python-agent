import json
from datetime import datetime

PATH = "output.json"

def save_output(log,parsed):
    entry = {
        "data":parsed,
        "timestamp":datetime.now().isoformat()
    }

    try:
        with open(PATH,"r") as f:
            d = json.load(f)
    except:
        d = []
    d.append(entry)

    with open(PATH,"w") as f:
        json.dump(d,f,indent = 4)