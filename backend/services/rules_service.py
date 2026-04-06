from database.db import db

rules_collection = db["rules"]

def get_rules():
    data = list(rules_collection.find())
    for d in data:
        d["_id"] = str(d["_id"])
    return data


def add_rule(rule):
    rules_collection.insert_one(rule)
    return {"message": "Rule added"}


def delete_rule(rule_id):
    from bson import ObjectId
    rules_collection.delete_one({"_id": ObjectId(rule_id)})
    return {"message": "Rule deleted"}