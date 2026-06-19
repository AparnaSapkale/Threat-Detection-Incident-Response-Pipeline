import requests
import time

CONFIG_API = "http://127.0.0.1:8001/admin/config"

config_cache = {

    "time_window": 10,

    "threshold": 5,

    "duplicate_window": 30,

    "auto_block": True,

    "correlation_enabled": True
}

last_fetch = 0

CACHE_TTL = 10


def get_config():

    global last_fetch

    current_time = time.time()

    # ---------------------------------------------------
    # FETCH CONFIG EVERY 10 SECONDS
    # ---------------------------------------------------

    if current_time - last_fetch > CACHE_TTL:

        try:

            res = requests.get(CONFIG_API)

            if res.status_code == 200:

                config_cache.update(res.json())

                last_fetch = current_time

                print("⚙️ Config Synced")

        except Exception as e:

            print("❌ Config Fetch Failed:", e)

    return config_cache
