from datetime import datetime

from database.db import blocked_ips_collection


def handle_soar(alert):

    # ---------------------------------------------------
    # ONLY BLOCK HIGH / CRITICAL
    # ---------------------------------------------------

    if alert.severity not in ["HIGH", "CRITICAL"]:
        return

    already_blocked = blocked_ips_collection.find_one({
        "ip": alert.ip
    })

    if already_blocked:
        return

    blocked_ips_collection.insert_one({

        "ip": alert.ip,

        "severity": alert.severity,

        "attack_type": alert.attack_type,

        "blocked_at": alert.timestamp,

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "reason": f"Auto-blocked due to {alert.attack_type}",

        "status": "BLOCKED"
    })

    print(
        f"🚫 AUTO-BLOCKED IP: {alert.ip} "
        f"| Severity: {alert.severity}"
    )

# from database.db import blocked_ips_collection

# def handle_soar(alert):

#     if alert.severity != "HIGH":
#         return

#     already_blocked = blocked_ips_collection.find_one({"ip": alert.ip})

#     if not already_blocked:
#         blocked_ips_collection.insert_one({
#             "ip": alert.ip,
#             "blocked_at": alert.timestamp,
#             "reason": "HIGH severity attack"
#         })

#         print(f"🚫 AUTO-BLOCKED IP: {alert.ip}")