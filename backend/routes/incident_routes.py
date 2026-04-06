from fastapi import APIRouter
from database.db import incidents_collection
from bson import ObjectId

router = APIRouter()

@router.get("/incidents")
def get_incidents():
    data = list(incidents_collection.find().sort("_id", -1))
    for d in data:
        d["_id"] = str(d["_id"])
    return data

@router.put("/incident/{incident_id}/close")
def close_incident(incident_id: str):
    incidents_collection.update_one(
        {"_id": ObjectId(incident_id)},
        {"$set": {"status": "CLOSED"}}
    )
    return {"message": "Incident closed"}