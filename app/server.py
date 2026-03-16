from fastapi import FastAPI
from app.processor import process_log

app = FastAPI()

@app.post("/ingest")

def ingest(log:str):

    process_log(log)

    return {"status":"ok"}