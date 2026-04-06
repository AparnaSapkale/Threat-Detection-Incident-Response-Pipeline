import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["SIEM-Database"]

alerts_collection = db["alerts"]
incidents_collection = db["incidents"]
blocked_ips_collection = db["blocked_ips"]