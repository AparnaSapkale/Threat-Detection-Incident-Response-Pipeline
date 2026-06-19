from datetime import datetime

from database.db import incidents_collection


def handle_incident(alert):

    existing = incidents_collection.find_one({

        "ip": alert.ip,
        "status": "OPEN"
    })

    # ---------------------------------------------------
    # UPDATE EXISTING INCIDENT
    # ---------------------------------------------------

    if existing:

        incidents_collection.update_one(

            {"_id": existing["_id"]},

            {
                "$set": {

                    "last_seen": alert.timestamp,

                    "severity": alert.severity,

                    "updated_at": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                },

                "$inc": {
                    "alert_count": 1
                },

                "$addToSet": {
                    "attack_types": alert.attack_type
                }
            }
        )

    # ---------------------------------------------------
    # CREATE NEW INCIDENT
    # ---------------------------------------------------

    else:

        incidents_collection.insert_one({

            "ip": alert.ip,

            "hostname": getattr(alert, "hostname", "UNKNOWN"),

            "attack_types": [alert.attack_type],

            "severity": alert.severity,

            "status": "OPEN",

            "priority": "P2",

            "first_seen": alert.timestamp,

            "last_seen": alert.timestamp,

            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "updated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "alert_count": 1,

            "assigned_to": None,

            "notes": []
        })

# from database.db import incidents_collection

# def handle_incident(alert):

#     existing = incidents_collection.find_one({
#         "ip": alert.ip,
#         "status": "OPEN"
#     })

#     if existing:
#         incidents_collection.update_one(
#             {"_id": existing["_id"]},
#             {
#                 "$set": {
#                     "last_seen": alert.timestamp,
#                     "severity": alert.severity
#                 },
#                 "$inc": {"alert_count": 1},
#                 "$addToSet": {"attack_types": alert.attack_type}
#             }
#         )
#     else:
#         incidents_collection.insert_one({
#             "ip": alert.ip,
#             "attack_types": [alert.attack_type],
#             "severity": alert.severity,
#             "status": "OPEN",
#             "first_seen": alert.timestamp,
#             "last_seen": alert.timestamp,
#             "alert_count": 1
#         })