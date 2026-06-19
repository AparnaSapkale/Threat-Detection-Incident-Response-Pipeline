import uuid
import socket
import requests

from datetime import datetime

from utils import get_network_type

from config import (
    API_URL,
    MONITOR_NAME
)

HOSTNAME = socket.gethostname()


def send_alert(
    ip,
    attack_type,
    severity,
    count,
    attack_count,
    tactic
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    payload = {

        "alert_id": str(uuid.uuid4()),

        "timestamp": timestamp,

        "ip": ip,

        "hostname": HOSTNAME,

        "attack_type": attack_type,

        "severity": severity,

        "ip_type": get_network_type(ip),

        "attack_count": attack_count,

        "tactic": tactic,

        "source": MONITOR_NAME,

        "status": "ACTIVE"
    }

    print(
        f"[{severity}] "
        f"{attack_type} | "
        f"{ip} | "
        f"Count: {count}"
    )

    try:

        res = requests.post(API_URL, json=payload)

        print(f"➡️ Alert Sent: {res.status_code}")

    except Exception as e:

        print("❌ Backend Error:", e)

# import requests
# from datetime import datetime
# from utils import get_network_type
# from config import API_URL

# def send_alert(ip, attack_type, severity, count, attack_count):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     network_type = get_network_type(ip)

#     payload = {
#         "timestamp": timestamp,
#         "ip": ip,
#         "attack_type": attack_type,
#         "severity": severity,
#         "ip_type": network_type,
#         "attack_count": attack_count
#     }

#     print(f"{severity} | {attack_type} | {ip} | Count: {count}")

#     try:
#         res = requests.post(API_URL, json=payload)
#         print("➡️ Sent:", res.status_code)
#     except Exception as e:
#         print("❌ Backend error:", e)