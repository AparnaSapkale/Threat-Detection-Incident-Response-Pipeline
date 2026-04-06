from fastapi import APIRouter
from database.db import alerts_collection
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/report/summary")
def get_report_summary():
    last_24h = datetime.now() - timedelta(hours=24)

    pipeline = [
        {"$match": {"timestamp": {"$gte": last_24h.strftime("%Y-%m-%d %H:%M:%S")}}},
        {"$group": {"_id": "$attack_type", "count": {"$sum": 1}}}
    ]

    result = list(alerts_collection.aggregate(pipeline))
    total_alerts = sum(r["count"] for r in result)

    return {
        "total_alerts": total_alerts,
        "attack_breakdown": result
    }

@router.get("/report/full")
def full_report():
    alerts = list(alerts_collection.find().sort("_id", -1).limit(100))
    for a in alerts:
        a["_id"] = str(a["_id"])

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "alerts": alerts
    }