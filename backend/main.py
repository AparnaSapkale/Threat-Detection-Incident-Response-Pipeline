from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# -------------------------------
# CORS CONFIG
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# STORAGE
# -------------------------------
alerts = []
MAX_ALERTS = 1000  # prevent memory overflow

# -------------------------------
# INCIDENT STORAGE
# -------------------------------
incidents = []
incident_counter = 1

# -------------------------------
# MODEL (UPDATED)
# -------------------------------
class Alert(BaseModel):
    timestamp: str
    ip: str
    attack_type: str
    severity: str
    ip_type: str          # NEW
    attack_count: int     # NEW


# -------------------------------
# INCIDENT MODEL
# -------------------------------
class Incident(BaseModel):
    id: int
    ip: str
    attack_types: list
    severity: str
    status: str
    first_seen: str
    last_seen: str
    alert_count: int


# -------------------------------
# ROUTES
# -------------------------------

@app.get("/")
def home():
    return {"message": "Mini SIEM Backend Running 🚀"}

# --------------------------------------------------------------------
@app.get("/alerts")
def get_alerts():
    # Return latest alerts first
    return list(reversed(alerts))

# --------------------------------------------------------------------
@app.post("/alert")
def receive_alert(alert: Alert):
    global incident_counter

    alert_data = alert.dict()

    # Store alert
    alerts.append(alert_data)

    # Limit memory
    if len(alerts) > MAX_ALERTS:
        alerts.pop(0)

    # -------------------------------
    # INCIDENT LOGIC
    # -------------------------------
    existing_incident = find_incident(alert.ip)

    if existing_incident:
        # Update incident
        existing_incident["last_seen"] = alert.timestamp
        existing_incident["alert_count"] += 1

        if alert.attack_type not in existing_incident["attack_types"]:
            existing_incident["attack_types"].append(alert.attack_type)

        # Upgrade severity if needed
        if alert.severity == "HIGH":
            existing_incident["severity"] = "HIGH"

    else:
        # Create new incident
        new_incident = {
            "id": incident_counter,
            "ip": alert.ip,
            "attack_types": [alert.attack_type],
            "severity": alert.severity,
            "status": "OPEN",
            "first_seen": alert.timestamp,
            "last_seen": alert.timestamp,
            "alert_count": 1
        }

        incidents.append(new_incident)
        incident_counter += 1

    return {"message": "Alert processed + Incident updated"}

# --------------------------------------------------------------------
@app.get("/alerts/filter")
def filter_alerts(ip: str = None, severity: str = None, attack_type: str = None):
    result = alerts

    if ip:
        result = [a for a in result if a["ip"] == ip]

    if severity:
        result = [a for a in result if a["severity"] == severity]

    if attack_type:
        result = [a for a in result if a["attack_type"] == attack_type]

    return list(reversed(result))
# --------------------------------------------------------------------
def find_incident(ip):
    for incident in incidents:
        if incident["ip"] == ip and incident["status"] == "OPEN":
            return incident
    return None

# --------------------------------------------------------------------
@app.get("/incidents")
def get_incidents():
    return list(reversed(incidents))

# --------------------------------------------------------------------
@app.get("/incident/{incident_id}")
def get_incident(incident_id: int):
    for incident in incidents:
        if incident["id"] == incident_id:
            return incident
    return {"error": "Incident not found"}

# --------------------------------------------------------------------
@app.put("/incident/{incident_id}/close")
def close_incident(incident_id: int):
    for incident in incidents:
        if incident["id"] == incident_id:
            incident["status"] = "CLOSED"
            return {"message": "Incident closed"}
    return {"error": "Incident not found"}

# --------------------------------------------------------------------
