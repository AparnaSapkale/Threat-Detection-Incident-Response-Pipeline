import time
from config import LOG_FILE
from detector import process_line

print("🚀 Advanced SOC Monitoring Started...\n")

with open(LOG_FILE, "r") as f:
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(1)
            continue

        process_line(line)

# To run the monitor, use the command: `python monitor/main_monitor.py`
# python monitor/main_monitor.py