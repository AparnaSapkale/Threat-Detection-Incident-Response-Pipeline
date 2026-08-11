from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from routes.alert_routes import router as alert_router
from routes.incident_routes import router as incident_router
from routes.dashboard_routes import router as dashboard_router
from routes.report_routes import router as report_router
from routes.stats_routes import router as stats_router

from services.config_service import (
    init_config,
    get_config,
    update_config
)

from services.rules_service import (
    get_rules,
    add_rule,
    delete_rule
)

from services.admin_service import (
    get_blocked_ips,
    unblock_ip
)

# ---------------------------------------------------
# FASTAPI INIT
# ---------------------------------------------------

app = FastAPI(
    title="Mini SIEM Platform",
    description="Threat Detection & Incident Response Backend",
    version="2.0"
)

# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        #allow_origins=["http://localhost:3000"],# Set explicit origins, this is old one # 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# STARTUP EVENT
# ---------------------------------------------------

@app.on_event("startup")
def startup_event():
    init_config()
    print("🚀 Mini SIEM Backend Started")

# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/", tags=["System"])
def home():
    return {
        "message": "Mini SIEM Backend Running 🚀",
        "status": "ACTIVE",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ---------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------

@app.get("/health", tags=["System"])
def health_check():
    return {
        "backend": "ONLINE",
        "api": "WORKING",
        "monitoring": "ACTIVE",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Health check 🚀",
    }

# ---------------------------------------------------
# SYSTEM STATUS
# ---------------------------------------------------

@app.get("/system/status", tags=["System"])
def system_status():
    return {
         "message": "system status 🚀",
        "backend_status": "RUNNING",
        "monitor_engine": "CONNECTED",
        "database": "CONNECTED",
        "alert_pipeline": "ACTIVE",
        "incident_engine": "ACTIVE",
        "soar_module": "READY"
    }

# ---------------------------------------------------
# ROUTES
# ---------------------------------------------------

app.include_router(alert_router, tags=["Alerts"])
app.include_router(incident_router, tags=["Incidents"])
app.include_router(dashboard_router, tags=["Dashboard"])
app.include_router(report_router, tags=["Reports"])
app.include_router(stats_router, tags=["Statistics"])

# ---------------------------------------------------
# CONFIG MANAGEMENT
# ---------------------------------------------------

@app.get("/admin/config", tags=["Admin"])
def read_config():
    return get_config()

@app.put("/admin/config", tags=["Admin"])
def edit_config(data: dict):
    return update_config(data)

# ---------------------------------------------------
# RULE MANAGEMENT
# ---------------------------------------------------

@app.get("/admin/rules", tags=["Rules"])
def read_rules():
    return get_rules()

@app.post("/admin/rules", tags=["Rules"])
def create_rule(rule: dict):
    return add_rule(rule)

@app.delete("/admin/rules/{rule_id}", tags=["Rules"])
def remove_rule(rule_id: str):
    return delete_rule(rule_id)

# ---------------------------------------------------
# BLOCKED IPS
# ---------------------------------------------------

@app.get("/admin/blocked-ips", tags=["SOAR"])
def read_blocked_ips():
    return get_blocked_ips()

@app.delete("/admin/unblock/{ip}", tags=["SOAR"])
def remove_block(ip: str):
    return unblock_ip(ip)