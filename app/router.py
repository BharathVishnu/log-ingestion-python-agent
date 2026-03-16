def route_log(log, classification):

    if classification == "security_incident":

        return "alert"

    elif classification == "suspicious":

        return "soc_dashboard"

    else:

        return "storage"