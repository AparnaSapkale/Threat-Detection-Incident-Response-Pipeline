from database.db import db
from bson import ObjectId

blocked_ips_collection = db["blocked_ips"]

def get_blocked_ips():
    data = list(blocked_ips_collection.find())
    for d in data:
        d["_id"] = str(d["_id"])
    return data


def unblock_ip(ip):
    blocked_ips_collection.delete_one({"ip": ip})
    return {"message": f"{ip} unblocked"}