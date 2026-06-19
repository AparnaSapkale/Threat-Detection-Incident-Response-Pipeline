from datetime import datetime

def log_info(message):

    print(
        f"[INFO] "
        f"{datetime.now()} | "
        f"{message}"
    )

def log_error(message):

    print(
        f"[ERROR] "
        f"{datetime.now()} | "
        f"{message}"
    )