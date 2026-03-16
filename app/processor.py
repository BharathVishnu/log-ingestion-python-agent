from llm.classifier import classify_log
from llm.normalizer import normalize_log
from enricher import enrich_log
from database import save_log
from router import route_log
from destination import send_alert, send_to_dashboard, store_log

def process_log(log):

    normalized = normalize_log(log)

    enriched = enrich_log(normalized)

    classification = classify_log(log)

    destination = route_log(enriched, classification)

    if destination == "alert":

        send_alert(enriched)

    elif destination == "soc_dashboard":

        send_to_dashboard(enriched)

    else:

        store_log(enriched)