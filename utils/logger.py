from datetime import datetime


def log_activity(message):

    with open("system_log.txt", "a") as file:

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"[{time}] {message}\n")
