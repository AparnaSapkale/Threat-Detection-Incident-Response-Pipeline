from database.db import db
from bson import ObjectId

from datetime import datetime

rules_collection = db["rules"]


def get_rules():

    data = list(
        rules_collection.find().sort("_id", -1)
    )

    for d in data:
        d["_id"] = str(d["_id"])

    return data


def add_rule(rule):

    rule["enabled"] = True

    rule["created_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    rules_collection.insert_one(rule)

    return {
        "status": "SUCCESS",
        "message": "Rule added successfully"
    }


def delete_rule(rule_id):

    result = rules_collection.delete_one({
        "_id": ObjectId(rule_id)
    })

    if result.deleted_count == 0:

        return {
            "status": "FAILED",
            "message": "Rule not found"
        }

    return {
        "status": "SUCCESS",
        "message": "Rule deleted successfully"
    }

# from database.db import db

# rules_collection = db["rules"]

# def get_rules():
#     data = list(rules_collection.find())
#     for d in data:
#         d["_id"] = str(d["_id"])
#     return data


# def add_rule(rule):
#     rules_collection.insert_one(rule)
#     return {"message": "Rule added"}


# def delete_rule(rule_id):
#     from bson import ObjectId
#     rules_collection.delete_one({"_id": ObjectId(rule_id)})
#     return {"message": "Rule deleted"}