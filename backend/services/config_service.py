from database.db import db

config_collection = db["config"]

# DEFAULT CONFIG (auto-create if empty)
def init_config():
    if config_collection.count_documents({}) == 0:
        config_collection.insert_one({
            "time_window": 10,
            "threshold": 5,
            "auto_block": True
        })


def get_config():
    return config_collection.find_one({}, {"_id": 0})


def update_config(data):
    config_collection.update_one({}, {"$set": data})
    return {"message": "Config updated"}