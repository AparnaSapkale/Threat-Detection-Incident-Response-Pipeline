from fastapi import APIRouter
from models.alert_model import Alert
from services.alert_service import process_alert
from database.db import alerts_collection

router = APIRouter()

@router.post("/alert")
def receive_alert(alert: Alert):
    return process_alert(alert)

@router.get("/alerts")
def get_alerts():
    data = list(alerts_collection.find().sort("_id", -1).limit(100))
    for d in data:
        d["_id"] = str(d["_id"])
    return data

@router.get("/alerts/filter")
def filter_alerts(ip: str = None):

    query = {}
    if ip:
        query["ip"] = ip

    data = list(alerts_collection.find(query).sort("_id", -1))

    for d in data:
        d["_id"] = str(d["_id"])

    return data