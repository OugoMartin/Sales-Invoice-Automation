from datetime import datetime

def log_run(status, message):
    """Log the run status and message."""
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {status} - {message}\n")
