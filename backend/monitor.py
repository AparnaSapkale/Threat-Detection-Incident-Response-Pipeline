import time
import re
import uuid
import socket
import requests
import ipaddress

from datetime import datetime
from collections import defaultdict, deque

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

LOG_FILE = "/var/log/auth.log"
API_URL = "http://127.0.0.1:8001/alert"

TIME_WINDOW = 10
THRESHOLD = 5
DUPLICATE_WINDOW = 30

HOSTNAME = socket.gethostname()

print("🚀 Advanced SOC Monitoring Engine Started...\n")

# ---------------------------------------------------
# MEMORY TRACKING
# ---------------------------------------------------

ip_attempts = defaultdict(lambda: deque())
recent_alerts = {}
event_history = defaultdict(set)
attack_count = defaultdict(int)

# ---------------------------------------------------
# HELPERS
# ---------------------------------------------------

def get_network_type(ip):
    try:
        return "PRIVATE" if ipaddress.ip_address(ip).is_private else "PUBLIC"
    except:
        return "UNKNOWN"

def is_duplicate(ip, attack_type):
    key = f"{ip}-{attack_type}"
    current_time = time.time()

    if key in recent_alerts:
        if current_time - recent_alerts[key] < DUPLICATE_WINDOW:
            return True

    recent_alerts[key] = current_time
    return False

def calculate_severity(ip):

    events = event_history[ip]

    if "BRUTE_FORCE" in events and "SCAN" in events:
        return "HIGH"

    if len(events) >= 3:
        return "CRITICAL"

    return "MEDIUM"

def generate_alert(
    ip,
    attack_type,
    count,
    tactic
):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    severity = calculate_severity(ip)

    payload = {
        "alert_id": str(uuid.uuid4()),
        "timestamp": timestamp,
        "ip": ip,
        "hostname": HOSTNAME,
        "attack_type": attack_type,
        "severity": severity,
        "ip_type": get_network_type(ip),
        "attack_count": attack_count[ip],
        "tactic": tactic,
        "source": "AUTH_LOG_MONITOR",
        "status": "ACTIVE"
    }

    return payload

# ---------------------------------------------------
# ALERT SENDER
# ---------------------------------------------------

def send_alert(payload):

    print(
        f"[{payload['severity']}] "
        f"{payload['attack_type']} | "
        f"{payload['ip']} | "
        f"Count: {payload['attack_count']}"
    )

    try:
        response = requests.post(API_URL, json=payload)

        print(f"➡️ Alert Sent: {response.status_code}")

    except Exception as e:
        print("❌ Backend Connection Error:", e)

# ---------------------------------------------------
# MAIN MONITOR LOOP
# ---------------------------------------------------

with open(LOG_FILE, "r") as f:

    f.seek(0, 2)

    while True:

        line = f.readline()

        if not line:
            time.sleep(1)
            continue

        now = datetime.now()

        # ---------------------------------------------------
        # SSH BRUTE FORCE
        # ---------------------------------------------------

        if "Failed password" in line:

            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

            if ip_match:

                ip = ip_match.group()

                ip_attempts[ip].append(now)

                while (
                    ip_attempts[ip]
                    and
                    (now - ip_attempts[ip][0]).seconds > TIME_WINDOW
                ):
                    ip_attempts[ip].popleft()

                count = len(ip_attempts[ip])

                if count >= THRESHOLD:

                    if not is_duplicate(ip, "BRUTE_FORCE"):

                        attack_count[ip] += 1

                        event_history[ip].add("BRUTE_FORCE")

                        payload = generate_alert(
                            ip,
                            "SSH Brute Force",
                            count,
                            "Credential Access"
                        )

                        send_alert(payload)

        # ---------------------------------------------------
        # NETWORK SCAN
        # ---------------------------------------------------

        if "Invalid user" in line or "Connection closed" in line:

            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

            if ip_match:

                ip = ip_match.group()

                ip_attempts[ip].append(now)

                while (
                    ip_attempts[ip]
                    and
                    (now - ip_attempts[ip][0]).seconds > TIME_WINDOW
                ):
                    ip_attempts[ip].popleft()

                count = len(ip_attempts[ip])

                if count >= THRESHOLD:

                    if not is_duplicate(ip, "SCAN"):

                        attack_count[ip] += 1

                        event_history[ip].add("SCAN")

                        payload = generate_alert(
                            ip,
                            "Network Scan",
                            count,
                            "Reconnaissance"
                        )

                        send_alert(payload)
