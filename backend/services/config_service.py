from database.db import db

config_collection = db["config"]


# ---------------------------------------------------
# DEFAULT CONFIG
# ---------------------------------------------------

def init_config():

    if config_collection.count_documents({}) == 0:

        config_collection.insert_one({

            "time_window": 10,
            "threshold": 5,

            "auto_block": True,

            "duplicate_window": 30,

            "correlation_enabled": True,

            "monitor_status": "ACTIVE",

            "alert_retention_days": 30
        })


# ---------------------------------------------------
# GET CONFIG
# ---------------------------------------------------

def get_config():

    return config_collection.find_one({}, {"_id": 0})


# ---------------------------------------------------
# UPDATE CONFIG
# ---------------------------------------------------

def update_config(data):

    config_collection.update_one(
        {},
        {"$set": data}
    )

    return {
        "status": "SUCCESS",
        "message": "Configuration updated"
    }

# from database.db import db

# config_collection = db["config"]

# # DEFAULT CONFIG (auto-create if empty)
# def init_config():
#     if config_collection.count_documents({}) == 0:
#         config_collection.insert_one({
#             "time_window": 10,
#             "threshold": 5,
#             "auto_block": True
#         })


# def get_config():
#     return config_collection.find_one({}, {"_id": 0})


# def update_config(data):
#     config_collection.update_one({}, {"$set": data})
#     return {"message": "Config updated"}