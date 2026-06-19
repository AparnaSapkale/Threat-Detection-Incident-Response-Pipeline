from fastapi import APIRouter

from database.db import (
    alerts_collection,
    incidents_collection,
    blocked_ips_collection
)

router = APIRouter(
    tags=["Statistics"]
)

# ---------------------------------------------------
# DASHBOARD STATS
# ---------------------------------------------------

@router.get("/stats")
def get_stats():

    total_alerts = alerts_collection.count_documents({})

    active_incidents = incidents_collection.count_documents({
        "status": "OPEN"
    })

    blocked_ips = blocked_ips_collection.count_documents({})

    return {

        "total_alerts": total_alerts,

        "active_incidents": active_incidents,

        "blocked_ips": blocked_ips,
        
        "assets_monitored": active_incidents
    }

# ---------------------------------------------------
# ALERTS BY SEVERITY
# ---------------------------------------------------

@router.get("/stats/alerts-by-severity")
def alerts_by_severity():

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

    return result

# from fastapi import APIRouter

# from database.db import alerts_collection

# router = APIRouter(
#     tags=["Statistics"]
# )

# # ---------------------------------------------------
# # ALERT TREND
# # ---------------------------------------------------

# @router.get("/stats/alerts-by-severity")
# def alerts_by_severity():

#     pipeline = [

#         {
#             "$group": {
#                 "_id": "$severity",
#                 "count": {"$sum": 1}
#             }
#         }
#     ]

#     result = list(
#         alerts_collection.aggregate(pipeline)
#     )

#     return result