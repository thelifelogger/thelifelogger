import datetime

def log_marker(marker_type="manual", description=""):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("marker_log.txt", "a") as f:
        f.write(f"{timestamp} | {marker_type} | {description}\n")
    print(f"Marker logged at {timestamp} ({marker_type})")

# Example usage
log_marker(marker_type="whistle", description="Interesting sound in recording")
log_marker(marker_type="tap", description="Smartwatch marker test")

