import re

from collections import defaultdict, deque
from datetime import datetime

from utils import (
    is_duplicate,
    calculate_severity
)

from sender import send_alert

from config_loader import get_config

# ---------------------------------------------------
# MEMORY TRACKING
# ---------------------------------------------------

ip_attempts = defaultdict(lambda: deque())

event_history = defaultdict(set)

attack_count = defaultdict(int)

# ---------------------------------------------------
# PROCESS LOG LINE
# ---------------------------------------------------

def process_line(line):

    config = get_config()

    TIME_WINDOW = config["time_window"]

    THRESHOLD = config["threshold"]

    DUPLICATE_WINDOW = config["duplicate_window"]

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

            if (
                count >= THRESHOLD
                and
                not is_duplicate(
                    ip,
                    "BRUTE_FORCE",
                    DUPLICATE_WINDOW
                )
            ):

                attack_count[ip] += 1

                event_history[ip].add("BRUTE_FORCE")

                severity = calculate_severity(
                    event_history[ip]
                )

                send_alert(
                    ip=ip,
                    attack_type="SSH Brute Force",
                    severity=severity,
                    count=count,
                    attack_count=attack_count[ip],
                    tactic="Credential Access"
                )

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

            if (
                count >= THRESHOLD
                and
                not is_duplicate(
                    ip,
                    "SCAN",
                    DUPLICATE_WINDOW
                )
            ):

                attack_count[ip] += 1

                event_history[ip].add("SCAN")

                severity = calculate_severity(
                    event_history[ip]
                )

                send_alert(
                    ip=ip,
                    attack_type="Network Scan",
                    severity=severity,
                    count=count,
                    attack_count=attack_count[ip],
                    tactic="Reconnaissance"
                )


# import re
# from collections import defaultdict, deque
# from datetime import datetime
# from utils import is_duplicate
# from sender import send_alert
# from config_loader import get_config
# from config import DUPLICATE_WINDOW

# ip_attempts = defaultdict(lambda: deque())
# event_history = defaultdict(set)
# attack_count = defaultdict(int)


# def check_correlation(ip):
#     events = event_history[ip]
#     if "SCAN" in events and "BRUTE_FORCE" in events:
#         return "HIGH"
#     return "MEDIUM"


# def process_line(line):
#     now = datetime.now()

#     # ---------------- SSH BRUTE FORCE ----------------
#     if "Failed password" in line:
#         ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

#         if ip_match:
#             ip = ip_match.group()
#             ip_attempts[ip].append(now)

#             while ip_attempts[ip] and (now - ip_attempts[ip][0]).seconds > TIME_WINDOW:
#                 ip_attempts[ip].popleft()

#             count = len(ip_attempts[ip])

#             if count >= THRESHOLD and not is_duplicate(ip, "BRUTE_FORCE", DUPLICATE_WINDOW):
#                 attack_count[ip] += 1
#                 event_history[ip].add("BRUTE_FORCE")

#                 severity = check_correlation(ip)
#                 send_alert(ip, "SSH Brute Force", severity, count, attack_count[ip])

#     # ---------------- NETWORK SCAN ----------------
#     if "Invalid user" in line or "Connection closed" in line:
#         ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

#         if ip_match:
#             ip = ip_match.group()
#             ip_attempts[ip].append(now)

#             while ip_attempts[ip] and (now - ip_attempts[ip][0]).seconds > TIME_WINDOW:
#                 ip_attempts[ip].popleft()

#             count = len(ip_attempts[ip])

#             if count >= THRESHOLD and not is_duplicate(ip, "SCAN", DUPLICATE_WINDOW):
#                 attack_count[ip] += 1
#                 event_history[ip].add("SCAN")

#                 severity = check_correlation(ip)
#                 send_alert(ip, "Network Scan", severity, count, attack_count[ip])