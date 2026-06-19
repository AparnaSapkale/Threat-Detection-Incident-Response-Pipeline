import time

from config import (
    LOG_FILE,
    MONITOR_NAME,
    MONITOR_VERSION
)

from detector import process_line

# ---------------------------------------------------
# STARTUP
# ---------------------------------------------------

print("\n" + "=" * 60)

print(f"🚀 {MONITOR_NAME} Started")

print(f"📌 Version: {MONITOR_VERSION}")

print(f"📂 Monitoring: {LOG_FILE}")

print("=" * 60 + "\n")

# ---------------------------------------------------
# LIVE LOG MONITORING
# ---------------------------------------------------

with open(LOG_FILE, "r") as f:

    f.seek(0, 2)

    while True:

        line = f.readline()

        if not line:

            time.sleep(1)

            continue

        process_line(line)

# import time
# from config import LOG_FILE
# from detector import process_line

# print("🚀 Advanced SOC Monitoring Started...\n")

# with open(LOG_FILE, "r") as f:
#     f.seek(0, 2)

#     while True:
#         line = f.readline()

#         if not line:
#             time.sleep(1)
#             continue

#         process_line(line)

# # To run the monitor, use the command: `python monitor/main_monitor.py`
# # python monitor/main_monitor.py