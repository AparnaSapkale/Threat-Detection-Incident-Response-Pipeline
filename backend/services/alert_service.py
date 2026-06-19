import uuid

from datetime import datetime

from database.db import alerts_collection

from services.incident_service import handle_incident
from services.soar_service import handle_soar


def process_alert(alert):

    alert_data = alert.dict()

    # ---------------------------------------------------
    # ENRICH ALERT
    # ---------------------------------------------------

    alert_data["alert_id"] = str(uuid.uuid4())

    alert_data["ingested_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    alert_data["status"] = "ACTIVE"

    # ---------------------------------------------------
    # STORE ALERT
    # ---------------------------------------------------

    alerts_collection.insert_one(alert_data)

    # ---------------------------------------------------
    # INCIDENT ENGINE
    # ---------------------------------------------------

    handle_incident(alert)

    # ---------------------------------------------------
    # SOAR ENGINE
    # ---------------------------------------------------

    handle_soar(alert)

    return {
        "status": "SUCCESS",
        "message": "Alert processed successfully",
        "alert_id": alert_data["alert_id"]
    }

# from database.db import alerts_collection
# from services.incident_service import handle_incident
# from services.soar_service import handle_soar

# def process_alert(alert):

#     alert_data = alert.dict()

#     # store alert
#     alerts_collection.insert_one(alert_data)

#     # incident logic
#     handle_incident(alert)

#     # soar logic
#     handle_soar(alert)

#     return {"message": "Alert processed successfully"}