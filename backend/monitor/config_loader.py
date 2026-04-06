import requests
import time

CONFIG_API = "http://127.0.0.1:8000/admin/config"

config_cache = {
    "time_window": 10,
    "threshold": 5,
    "auto_block": True
}

last_fetch = 0
CACHE_TTL = 10  # seconds


def get_config():
    global last_fetch

    current_time = time.time()

    # Fetch only every 10 sec (avoid API spam)
    if current_time - last_fetch > CACHE_TTL:
        try:
            res = requests.get(CONFIG_API)
            if res.status_code == 200:
                config_cache.update(res.json())
                last_fetch = current_time
                print("⚙️ Config Updated:", config_cache)
        except:
            print("❌ Config fetch failed (using old config)")

    return config_cache