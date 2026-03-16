from app.llm.classifier import classify_log
from app.llm.normalizer import normalize_log
from app.enricher import enrich_log
from app.database import save_log


from app.router import route_log
from app.destination import send_alert, send_to_dashboard, store_log

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