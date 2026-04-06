from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.alert_routes import router as alert_router
from routes.incident_routes import router as incident_router
from routes.dashboard_routes import router as dashboard_router
from routes.report_routes import router as report_router


from services.config_service import init_config, get_config, update_config
from services.rules_service import get_rules, add_rule, delete_rule
from services.admin_service import get_blocked_ips, unblock_ip

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



init_config()  # Initialize default config on startup


@app.get("/")
def home():
    return {"message": "Mini SIEM Backend Running 🚀"}

# include routes
app.include_router(alert_router)
app.include_router(incident_router)
app.include_router(dashboard_router)
app.include_router(report_router)



# CONFIG APIs

@app.get("/admin/config")
def read_config():
    return get_config()


@app.put("/admin/config")
def edit_config(data: dict):
    return update_config(data)

# RULE MANAGEMENT
@app.get("/admin/rules")
def read_rules():
    return get_rules()


@app.post("/admin/rules")
def create_rule(rule: dict):
    return add_rule(rule)


@app.delete("/admin/rules/{rule_id}")
def remove_rule(rule_id: str):
    return delete_rule(rule_id)

# BLOCKED IP MANAGEMENT

@app.get("/admin/blocked-ips")
def read_blocked_ips():
    return get_blocked_ips()


@app.delete("/admin/unblock/{ip}")
def remove_block(ip: str):
    return unblock_ip(ip)
    













# import os
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from dotenv import load_dotenv
# from pymongo import MongoClient
# from datetime import datetime, timedelta
# from bson import ObjectId

# # -------------------------------
# # LOAD ENV
# # -------------------------------
# load_dotenv()
# MONGO_URL = os.getenv("MONGO_URL")

# client = MongoClient(MONGO_URL)
# db = client["SIEM-Database"]

# alerts_collection = db["alerts"]
# incidents_collection = db["incidents"]
# blocked_ips_collection = db["blocked_ips"]

# # -------------------------------
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -------------------------------
# # MODEL
# # -------------------------------
# class Alert(BaseModel):
#     timestamp: str
#     ip: str
#     attack_type: str
#     severity: str
#     ip_type: str
#     attack_count: int

# # -------------------------------
# @app.get("/")
# def home():
#     return {"message": "Mini SIEM Backend Running 🚀"}

# # -------------------------------
# @app.get("/alerts")
# def get_alerts():
#     data = list(alerts_collection.find().sort("_id", -1).limit(100))
#     for d in data:
#         d["_id"] = str(d["_id"])
#     return data

# # -------------------------------
# @app.post("/alert")
# def receive_alert(alert: Alert):

#     alert_data = alert.dict()

#     # STORE ALERT
#     alerts_collection.insert_one(alert_data)

#     # INCIDENT LOGIC
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

#     # -------------------------------
#     # AUTO RESPONSE (SOAR)
#     # -------------------------------
#     if alert.severity == "HIGH":

#         already_blocked = blocked_ips_collection.find_one({"ip": alert.ip})

#         if not already_blocked:
#             try:
#                 # SAFE MODE
#                 # os.system(f"sudo iptables -A INPUT -s {alert.ip} -j DROP")

#                 blocked_ips_collection.insert_one({
#                     "ip": alert.ip,
#                     "blocked_at": alert.timestamp,
#                     "reason": "HIGH severity attack"
#                 })

#                 print(f"🚫 AUTO-BLOCKED IP: {alert.ip}")

#             except Exception as e:
#                 print("Block error:", e)

#     return {"message": "Alert stored + Incident updated + SOAR executed"}

# # -------------------------------
# @app.get("/incidents")
# def get_incidents():
#     data = list(incidents_collection.find().sort("_id", -1))
#     for d in data:
#         d["_id"] = str(d["_id"])
#     return data

# # -------------------------------
# @app.get("/blocked-ips")
# def get_blocked_ips():
#     data = list(blocked_ips_collection.find())
#     for d in data:
#         d["_id"] = str(d["_id"])
#     return data

# # -------------------------------
# @app.get("/stats")
# def get_stats():
#     return {
#         "total_alerts": alerts_collection.count_documents({}),
#         "active_incidents": incidents_collection.count_documents({"status": "OPEN"}),
#         "blocked_ips": blocked_ips_collection.count_documents({})
#     }

# # -------------------------------
# @app.get("/top-ips")
# def top_ips():
#     pipeline = [
#         {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 5}
#     ]
#     result = list(alerts_collection.aggregate(pipeline))
#     return [{"ip": r["_id"], "count": r["count"]} for r in result]

# # -------------------------------
# @app.get("/attack-stats")
# def attack_stats():
#     pipeline = [
#         {"$group": {"_id": "$attack_type", "count": {"$sum": 1}}}
#     ]
#     result = list(alerts_collection.aggregate(pipeline))
#     return [{"attack_type": r["_id"], "count": r["count"]} for r in result]

# # -------------------------------
# @app.get("/report/summary")
# def get_report_summary():
#     last_24h = datetime.now() - timedelta(hours=24)

#     pipeline = [
#         {"$match": {"timestamp": {"$gte": last_24h.strftime("%Y-%m-%d %H:%M:%S")}}},
#         {"$group": {"_id": "$attack_type", "count": {"$sum": 1}}}
#     ]

#     result = list(alerts_collection.aggregate(pipeline))
#     total_alerts = sum(r["count"] for r in result)

#     return {
#         "total_alerts": total_alerts,
#         "attack_breakdown": result
#     }

# # -------------------------------
# @app.get("/report/top-attacker")
# def top_attacker():
#     pipeline = [
#         {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 1}
#     ]

#     result = list(alerts_collection.aggregate(pipeline))

#     if result:
#         return {"ip": result[0]["_id"], "count": result[0]["count"]}
#     return {}

# # -------------------------------
# @app.get("/report/full")
# def full_report():
#     alerts = list(alerts_collection.find().sort("_id", -1).limit(100))
#     for a in alerts:
#         a["_id"] = str(a["_id"]

# )
#     return {
#         "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "alerts": alerts
#     }
# # import os
# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from fastapi.middleware.cors import CORSMiddleware
# # from dotenv import load_dotenv
# # from pymongo import MongoClient
# # from datetime import datetime, timedelta

# # # -------------------------------
# # # LOAD ENV
# # # -------------------------------
# # load_dotenv()
# # MONGO_URL = os.getenv("MONGO_URL")

# # client = MongoClient(MONGO_URL)
# # db = client["SIEM-Database"]

# # alerts_collection = db["alerts"]
# # incidents_collection = db["incidents"]
# # blocked_ips_collection = db["blocked_ips"]

# # # -------------------------------
# # app = FastAPI()
# # blocked_ips = set()

# # # -------------------------------
# # # CORS CONFIG
# # # -------------------------------
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # -------------------------------
# # # MODEL
# # # -------------------------------
# # class Alert(BaseModel):
# #     timestamp: str
# #     ip: str
# #     attack_type: str
# #     severity: str
# #     ip_type: str
# #     attack_count: int


# # # -------------------------------
# # # ROUTES
# # # -------------------------------

# # @app.get("/")
# # def home():
# #     return {"message": "Mini SIEM Backend Running 🚀"}

# # # --------------------------------------------------------------------
# # @app.get("/alerts")
# # def get_alerts():
# #     data = list(alerts_collection.find().sort("_id", -1).limit(100))
# #     for d in data:
# #         d["_id"] = str(d["_id"])
# #     return data

# # # --------------------------------------------------------------------
# # @app.post("/alert")
# # def receive_alert(alert: Alert):

# #     alert_data = alert.dict()

# #     # 🔥 STORE ALERT IN DB
# #     alerts_collection.insert_one(alert_data)

# #     # -------------------------------
# #     # INCIDENT LOGIC (DB VERSION)
# #     # -------------------------------
# #     existing = incidents_collection.find_one({
# #         "ip": alert.ip,
# #         "status": "OPEN"
# #     })

# #     if existing:
# #         incidents_collection.update_one(
# #             {"_id": existing["_id"]},
# #             {
# #                 "$set": {
# #                     "last_seen": alert.timestamp,
# #                     "severity": alert.severity
# #                 },
# #                 "$inc": {"alert_count": 1},
# #                 "$addToSet": {"attack_types": alert.attack_type}
# #             }
# #         )
# #     else:
# #         incidents_collection.insert_one({
# #             "ip": alert.ip,
# #             "attack_types": [alert.attack_type],
# #             "severity": alert.severity,
# #             "status": "OPEN",
# #             "first_seen": alert.timestamp,
# #             "last_seen": alert.timestamp,
# #             "alert_count": 1
# #         })

# #     # -------------------------------
# #     # AUTO RESPONSE (SOAR)
# #     # -------------------------------
# #     if alert.severity == "HIGH":

# #         already_blocked = blocked_ips_collection.find_one({"ip": alert.ip})

# #         if not already_blocked:
# #             try:
# #                 # 🔥 SAFE MODE (no real block yet)
# #                 # os.system(f"sudo iptables -A INPUT -s {alert.ip} -j DROP")

# #                 blocked_ips_collection.insert_one({
# #                     "ip": alert.ip,
# #                     "blocked_at": alert.timestamp,
# #                     "reason": "HIGH severity attack"
# #                 })

# #                 print(f"🚫 AUTO-BLOCKED IP: {alert.ip}")

# #             except Exception as e:
# #                 print("Block error:", e)

# #     return {"message": "Alert stored in DB + Incident updated + SOAR executed"}
# # # --------------------------------------------------------------------
# # @app.get("/alerts/filter")
# # def filter_alerts(ip: str = None):

# #     query = {}
# #     if ip:
# #         query["ip"] = ip

# #     data = list(alerts_collection.find(query).sort("_id", -1))

# #     for d in data:
# #         d["_id"] = str(d["_id"])

# #     return data

# # # --------------------------------------------------------------------
# @app.get("/incidents")
# def get_incidents():
#     data = list(incidents_collection.find().sort("_id", -1))
    
#     for d in data:
#         d["_id"] = str(d["_id"])   # 🔥 VERY IMPORTANT
    
#     return data   

# # # --------------------------------------------------------------------
# @app.put("/incident/{incident_id}/close")
# def close_incident(incident_id: str):
#     try:
#         incidents_collection.update_one(
#             {"_id": ObjectId(incident_id)},
#             {"$set": {"status": "CLOSED"}}
#         )
#         return {"message": "Incident closed"}
#     except Exception as e:
#         return {"error": str(e)}
# # # --------------------------------------------------------------------

# # # 
# # @app.post("/block_ip")
# # def block_ip(ip: str):

# #     if blocked_ips_collection.find_one({"ip": ip}):
# #         return {"message": "IP already blocked"}

# #     blocked_ips_collection.insert_one({
# #         "ip": ip
# #     })

# #     return {"message": f"{ip} blocked successfully"}

# # # --------------------------------------------------------------------
# # @app.get("/test-db")
# # def test_db():
# #     alerts_collection.insert_one({"test": "working"})
# #     return {"message": "DB working"}

# # # --------------------------------------------------------------------
# # @app.get("/stats")
# # def get_stats():
# #     total_alerts = alerts_collection.count_documents({})
# #     active_incidents = incidents_collection.count_documents({"status": "OPEN"})
# #     blocked_ips = blocked_ips_collection.count_documents({})

# #     return {
# #         "total_alerts": total_alerts,
# #         "active_incidents": active_incidents,
# #         "blocked_ips": blocked_ips
# #     }
# # # --------------------------------------------------------------------
# # @app.get("/top-ips")
# # def top_ips():
# #     pipeline = [
# #         {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
# #         {"$sort": {"count": -1}},
# #         {"$limit": 5}
# #     ]

# #     result = list(alerts_collection.aggregate(pipeline))

# #     return [
# #         {"ip": r["_id"], "count": r["count"]}
# #         for r in result
# #     ]
# # # --------------------------------------------------------------------
# # @app.get("/attack-stats")
# # def attack_stats():
# #     pipeline = [
# #         {"$group": {"_id": "$attack_type", "count": {"$sum": 1}}}
# #     ]

# #     result = list(alerts_collection.aggregate(pipeline))

# #     return [
# #         {"attack_type": r["_id"], "count": r["count"]}
# #         for r in result
# #     ]
# # # --------------------------------------------------------------------
# # @app.get("/blocked-ips")
# # def get_blocked_ips():
# #     data = list(blocked_ips_collection.find())
# #     for d in data:
# #         d["_id"] = str(d["_id"])
# #     return data
# # # --------------------------------------------------------------------


# # @app.get("/report/summary")
# # def get_report_summary():

# #     last_24h = datetime.now() - timedelta(hours=24)

# #     pipeline = [
# #         {
# #             "$match": {
# #                 "timestamp": {
# #                     "$gte": last_24h.strftime("%Y-%m-%d %H:%M:%S")
# #                 }
# #             }
# #         },
# #         {
# #             "$group": {
# #                 "_id": "$attack_type",
# #                 "count": {"$sum": 1}
# #             }
# #         }
# #     ]

# #     result = list(alerts_collection.aggregate(pipeline))

# #     total_alerts = sum(r["count"] for r in result)

# #     return {
# #         "total_alerts": total_alerts,
# #         "attack_breakdown": result
# #     }
# # # --------------------------------------------------------------------
# # @app.get("/report/top-attacker")
# # def top_attacker():

# #     pipeline = [
# #         {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
# #         {"$sort": {"count": -1}},
# #         {"$limit": 1}
# #     ]

# #     result = list(alerts_collection.aggregate(pipeline))

# #     if result:
# #         return {
# #             "ip": result[0]["_id"],
# #             "count": result[0]["count"]
# #         }

# #     return {}
# # # --------------------------------------------------------------------
# # @app.get("/report/full")
# # def full_report():

# #     alerts = list(alerts_collection.find().sort("_id", -1).limit(100))

# #     for a in alerts:
# #         a["_id"] = str(a["_id"])

# #     return {
# #         "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
# #         "alerts": alerts
# #     }
