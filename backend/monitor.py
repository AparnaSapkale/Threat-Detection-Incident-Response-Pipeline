import time
import re
import requests
from datetime import datetime
from collections import defaultdict, deque
import ipaddress

LOG_FILE = "/var/log/auth.log"
ALERT_FILE = "alerts.log"
API_URL = "http://127.0.0.1:8000/alert"

TIME_WINDOW = 10
THRESHOLD = 5
DUPLICATE_WINDOW = 30

print("🚀 Advanced SOC Monitoring Started...\n")

ip_attempts = defaultdict(lambda: deque())
recent_alerts = {}
event_history = defaultdict(set)
attack_count = defaultdict(int)

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

def check_correlation(ip):
    events = event_history[ip]
    if "SCAN" in events and "BRUTE_FORCE" in events:
        return "HIGH"
    return "MEDIUM"

def send_alert(ip, attack_type, severity, count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    network_type = get_network_type(ip)

    payload = {
        "timestamp": timestamp,
        "ip": ip,
        "attack_type": attack_type,
        "severity": severity,
        "ip_type": network_type,
        "attack_count": attack_count[ip]
    }

    print(f"{severity} | {attack_type} | {ip} | Count: {count}")

    try:
        res = requests.post(API_URL, json=payload)
        print("➡️ Sent:", res.status_code)
    except Exception as e:
        print("❌ Backend error:", e)

with open(LOG_FILE, "r") as f:
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(1)
            continue

        now = datetime.now()

        if "Failed password" in line:
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

            if ip_match:
                ip = ip_match.group()
                ip_attempts[ip].append(now)

                while ip_attempts[ip] and (now - ip_attempts[ip][0]).seconds > TIME_WINDOW:
                    ip_attempts[ip].popleft()

                count = len(ip_attempts[ip])

                if count >= THRESHOLD and not is_duplicate(ip, "BRUTE_FORCE"):
                    attack_count[ip] += 1
                    event_history[ip].add("BRUTE_FORCE")
                    severity = check_correlation(ip)
                    send_alert(ip, "SSH Brute Force", severity, count)

        if "Invalid user" in line or "Connection closed" in line:
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

            if ip_match:
                ip = ip_match.group()
                ip_attempts[ip].append(now)

                while ip_attempts[ip] and (now - ip_attempts[ip][0]).seconds > TIME_WINDOW:
                    ip_attempts[ip].popleft()

                count = len(ip_attempts[ip])

                if count >= THRESHOLD and not is_duplicate(ip, "SCAN"):
                    attack_count[ip] += 1
                    event_history[ip].add("SCAN")
                    severity = check_correlation(ip)
                    send_alert(ip, "Network Scan", severity, count)

# import time
# import re
# import requests
# from datetime import datetime
# from collections import defaultdict, deque
# import ipaddress

# LOG_FILE = "/var/log/auth.log"
# ALERT_FILE = "alerts.log"
# API_URL = "http://127.0.0.1:8000/alert"

# TIME_WINDOW = 10
# THRESHOLD = 5
# DUPLICATE_WINDOW = 30

# print("🚀 Advanced SOC Monitoring Started...\n")

# ip_attempts = defaultdict(lambda: deque())
# recent_alerts = {}
# event_history = defaultdict(set)
# attack_count = defaultdict(int)


# def get_network_type(ip):
#     try:
#         return "PRIVATE" if ipaddress.ip_address(ip).is_private else "PUBLIC"
#     except:
#         return "UNKNOWN"


# def is_duplicate(ip, attack_type):
#     key = f"{ip}-{attack_type}"
#     current_time = time.time()

#     if key in recent_alerts:
#         if current_time - recent_alerts[key] < DUPLICATE_WINDOW:
#             return True

#     recent_alerts[key] = current_time
#     return False


# def check_correlation(ip):
#     events = event_history[ip]
#     if "SCAN" in events and "BRUTE_FORCE" in events:
#         return "HIGH"
#     return "MEDIUM"


# def send_alert(ip, attack_type, severity, count):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     network_type = get_network_type(ip)

#     alert_msg = (
#         f"[{timestamp}] {severity} | {attack_type} | "
#         f"IP: {ip} ({network_type}) | Count(10s): {count} | Total: {attack_count[ip]}"
#     )

#     print(alert_msg)

#     with open(ALERT_FILE, "a") as af:
#         af.write(alert_msg + "\n")

#     payload = {
#         "timestamp": timestamp,
#         "ip": ip,
#         "attack_type": attack_type,
#         "severity": severity,
#         "ip_type": network_type,
#         "attack_count": attack_count[ip]
#     }

#     try:
#         res = requests.post(API_URL, json=payload)
#         print("➡️ Sent:", res.status_code)
#     except Exception as e:
#         print("❌ Backend error:", e)


# with open(LOG_FILE, "r") as f:
#     f.seek(0, 2)

#     while True:
#         line = f.readline()

#         if not line:
#             time.sleep(1)
#             continue

#         now = datetime.now()

#         # SSH BRUTE FORCE
#         if "Failed password" in line:

#             ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
#             repeat_match = re.search(r'message repeated (\d+) times', line)

#             attempts = 1
#             if repeat_match:
#                 attempts += int(repeat_match.group(1))

#             if ip_match:
#                 ip = ip_match.group()

#                 for _ in range(attempts):
#                     ip_attempts[ip].append(now)

#                 while ip_attempts[ip] and (now - ip_attempts[ip][0]).seconds > TIME_WINDOW:
#                     ip_attempts[ip].popleft()

#                 count = len(ip_attempts[ip])

#                 if count >= THRESHOLD:
#                     if not is_duplicate(ip, "BRUTE_FORCE"):
#                         attack_count[ip] += 1
#                         event_history[ip].add("BRUTE_FORCE")
#                         severity = check_correlation(ip)
#                         send_alert(ip, "SSH Brute Force", severity, count)

#         # NETWORK SCAN
#         if "Invalid user" in line or "Connection closed" in line:

#             ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

#             if ip_match:
#                 ip = ip_match.group()

#                 ip_attempts[ip].append(now)

#                 while ip_attempts[ip] and (now - ip_attempts[ip][0]).seconds > TIME_WINDOW:
#                     ip_attempts[ip].popleft()

#                 count = len(ip_attempts[ip])

#                 if count >= THRESHOLD:
#                     if not is_duplicate(ip, "SCAN"):
#                         attack_count[ip] += 1
#                         event_history[ip].add("SCAN")
#                         severity = check_correlation(ip)
#                         send_alert(ip, "Network Scan", severity, count)

#         # REVERSE SHELL
#         if "session opened" in line and "root" in line:

#             ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

#             if ip_match:
#                 ip = ip_match.group()

#                 if not is_duplicate(ip, "REVERSE_SHELL"):
#                     attack_count[ip] += 1
#                     event_history[ip].add("REVERSE_SHELL")
#                     send_alert(ip, "Possible Reverse Shell", "HIGH", 1)