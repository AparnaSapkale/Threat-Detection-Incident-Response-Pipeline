from database.db import blocked_ips_collection

def handle_soar(alert):

    if alert.severity != "HIGH":
        return

    already_blocked = blocked_ips_collection.find_one({"ip": alert.ip})

    if not already_blocked:
        blocked_ips_collection.insert_one({
            "ip": alert.ip,
            "blocked_at": alert.timestamp,
            "reason": "HIGH severity attack"
        })

        print(f"🚫 AUTO-BLOCKED IP: {alert.ip}")