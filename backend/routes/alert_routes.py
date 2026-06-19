from fastapi import APIRouter

from models.alert_model import Alert

from services.alert_service import process_alert

from database.db import alerts_collection

router = APIRouter(
    tags=["Alerts"]
)

# ---------------------------------------------------
# RECEIVE ALERT
# ---------------------------------------------------

@router.post("/alert")
def receive_alert(alert: Alert):

    return process_alert(alert)

# ---------------------------------------------------
# GET ALERTS
# ---------------------------------------------------

@router.get("/alerts")
def get_alerts(limit: int = 100):

    data = list(
        alerts_collection.find()
        .sort("_id", -1)
        .limit(limit)
    )

    for d in data:
        d["_id"] = str(d["_id"])

    return {
        "count": len(data),
        "alerts": data
    }

# ---------------------------------------------------
# FILTER ALERTS
# ---------------------------------------------------

@router.get("/alerts/filter")
def filter_alerts(

    ip: str = None,

    severity: str = None,

    attack_type: str = None
):

    query = {}

    if ip:
        query["ip"] = ip

    if severity:
        query["severity"] = severity.upper()

    if attack_type:
        query["attack_type"] = attack_type

    data = list(
        alerts_collection.find(query)
        .sort("_id", -1)
    )

    for d in data:
        d["_id"] = str(d["_id"])

    return {
        "count": len(data),
        "alerts": data
    }

# ---------------------------------------------------
# RECENT ALERTS
# ---------------------------------------------------

@router.get("/alerts/recent")
def recent_alerts():

    data = list(
        alerts_collection.find()
        .sort("_id", -1)
        .limit(10)
    )

    for d in data:
        d["_id"] = str(d["_id"])

    return data

# from fastapi import APIRouter
# from models.alert_model import Alert
# from services.alert_service import process_alert
# from database.db import alerts_collection

# router = APIRouter()

# @router.post("/alert")
# def receive_alert(alert: Alert):
#     return process_alert(alert)

# @router.get("/alerts")
# def get_alerts():
#     data = list(alerts_collection.find().sort("_id", -1).limit(100))
#     for d in data:
#         d["_id"] = str(d["_id"])
#     return data

# @router.get("/alerts/filter")
# def filter_alerts(ip: str = None):

#     query = {}
#     if ip:
#         query["ip"] = ip

#     data = list(alerts_collection.find(query).sort("_id", -1))

#     for d in data:
#         d["_id"] = str(d["_id"])

#     return data