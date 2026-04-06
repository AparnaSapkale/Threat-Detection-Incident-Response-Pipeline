import requests
from datetime import datetime
from utils import get_network_type
from config import API_URL

def send_alert(ip, attack_type, severity, count, attack_count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    network_type = get_network_type(ip)

    payload = {
        "timestamp": timestamp,
        "ip": ip,
        "attack_type": attack_type,
        "severity": severity,
        "ip_type": network_type,
        "attack_count": attack_count
    }

    print(f"{severity} | {attack_type} | {ip} | Count: {count}")

    try:
        res = requests.post(API_URL, json=payload)
        print("➡️ Sent:", res.status_code)
    except Exception as e:
        print("❌ Backend error:", e)