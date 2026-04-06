from database.db import incidents_collection

def handle_incident(alert):

    existing = incidents_collection.find_one({
        "ip": alert.ip,
        "status": "OPEN"
    })

    if existing:
        incidents_collection.update_one(
            {"_id": existing["_id"]},
            {
                "$set": {
                    "last_seen": alert.timestamp,
                    "severity": alert.severity
                },
                "$inc": {"alert_count": 1},
                "$addToSet": {"attack_types": alert.attack_type}
            }
        )
    else:
        incidents_collection.insert_one({
            "ip": alert.ip,
            "attack_types": [alert.attack_type],
            "severity": alert.severity,
            "status": "OPEN",
            "first_seen": alert.timestamp,
            "last_seen": alert.timestamp,
            "alert_count": 1
        })