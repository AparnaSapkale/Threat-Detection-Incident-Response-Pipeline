from database.db import alerts_collection
from services.incident_service import handle_incident
from services.soar_service import handle_soar

def process_alert(alert):

    alert_data = alert.dict()

    # store alert
    alerts_collection.insert_one(alert_data)

    # incident logic
    handle_incident(alert)

    # soar logic
    handle_soar(alert)

    return {"message": "Alert processed successfully"}