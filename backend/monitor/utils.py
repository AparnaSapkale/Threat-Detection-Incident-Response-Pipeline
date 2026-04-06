import time
import ipaddress

recent_alerts = {}

def get_network_type(ip):
    try:
        return "PRIVATE" if ipaddress.ip_address(ip).is_private else "PUBLIC"
    except:
        return "UNKNOWN"


def is_duplicate(ip, attack_type, window):
    key = f"{ip}-{attack_type}"
    current_time = time.time()

    if key in recent_alerts:
        if current_time - recent_alerts[key] < window:
            return True

    recent_alerts[key] = current_time
    return False