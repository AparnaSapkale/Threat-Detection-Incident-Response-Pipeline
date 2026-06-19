from fastapi import APIRouter

from database.db import (
    alerts_collection,
    incidents_collection,
    blocked_ips_collection
)

router = APIRouter(
    tags=["Dashboard"]
)

# ---------------------------------------------------
# MAIN STATS
# ---------------------------------------------------

@router.get("/stats")
def get_stats():

    return {

        "total_alerts":
        alerts_collection.count_documents({}),

        "active_incidents":
        incidents_collection.count_documents({
            "status": "OPEN"
        }),

        "blocked_ips":
        blocked_ips_collection.count_documents({}),

        "critical_alerts":
        alerts_collection.count_documents({
            "severity": "CRITICAL"
        }),

        "high_alerts":
        alerts_collection.count_documents({
            "severity": "HIGH"
        })
    }

# ---------------------------------------------------
# TOP ATTACKER IPS
# ---------------------------------------------------

@router.get("/top-ips")
def top_ips():

    pipeline = [

        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },

        {
            "$sort": {
                "count": -1
            }
        },

        {
            "$limit": 5
        }
    ]

    result = list(
        alerts_collection.aggregate(pipeline)
    )

    return [
        {
            "ip": r["_id"],
            "count": r["count"]
        }
        for r in result
    ]

# ---------------------------------------------------
# ATTACK STATS
# ---------------------------------------------------

@router.get("/attack-stats")
def attack_stats():

    pipeline = [

        {
            "$group": {
                "_id": "$attack_type",
                "count": {"$sum": 1}
            }
        }
    ]

    result = list(
        alerts_collection.aggregate(pipeline)
    )

    return [
        {
            "attack_type": r["_id"],
            "count": r["count"]
        }
        for r in result
    ]

# ---------------------------------------------------
# SEVERITY STATS
# ---------------------------------------------------

@router.get("/severity-stats")
def severity_stats():

    pipeline = [

        {
            "$group": {
                "_id": "$severity",
                "count": {"$sum": 1}
            }
        }
    ]

    result = list(
        alerts_collection.aggregate(pipeline)
    )

    return [
        {
            "severity": r["_id"],
            "count": r["count"]
        }
        for r in result
    ]


# from fastapi import APIRouter
# from database.db import alerts_collection, incidents_collection, blocked_ips_collection

# router = APIRouter()

# @router.get("/stats")
# def get_stats():
#     return {
#         "total_alerts": alerts_collection.count_documents({}),
#         "active_incidents": incidents_collection.count_documents({"status": "OPEN"}),
#         "blocked_ips": blocked_ips_collection.count_documents({})
#     }

# @router.get("/top-ips")
# def top_ips():
#     pipeline = [
#         {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 5}
#     ]
#     result = list(alerts_collection.aggregate(pipeline))
#     return [{"ip": r["_id"], "count": r["count"]} for r in result]

# @router.get("/attack-stats")
# def attack_stats():
#     pipeline = [
#         {"$group": {"_id": "$attack_type", "count": {"$sum": 1}}}
#     ]
#     result = list(alerts_collection.aggregate(pipeline))
#     return [{"attack_type": r["_id"], "count": r["count"]} for r in result]