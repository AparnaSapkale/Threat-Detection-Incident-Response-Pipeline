from database.db import db
from bson import ObjectId
from datetime import datetime

blocked_ips_collection = db["blocked_ips"]


def get_blocked_ips():

    data = list(
        blocked_ips_collection.find().sort("_id", -1)
    )

    for d in data:
        d["_id"] = str(d["_id"])

    return data


def unblock_ip(ip):

    result = blocked_ips_collection.delete_one({"ip": ip})

    if result.deleted_count == 0:
        return {
            "status": "FAILED",
            "message": f"{ip} not found"
        }

    return {
        "status": "SUCCESS",
        "message": f"{ip} unblocked successfully",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# from database.db import db
# from bson import ObjectId

# blocked_ips_collection = db["blocked_ips"]

# def get_blocked_ips():
#     data = list(blocked_ips_collection.find())
#     for d in data:
#         d["_id"] = str(d["_id"])
#     return data


# def unblock_ip(ip):
#     blocked_ips_collection.delete_one({"ip": ip})
#     return {"message": f"{ip} unblocked"}