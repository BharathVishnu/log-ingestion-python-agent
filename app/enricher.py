def enrich_log(log):

    ip = log.get("source_ip")

    if ip:

        if ip.startswith("192.168"):
            log["network_zone"] = "internal"

        else:
            log["network_zone"] = "external"

    return log