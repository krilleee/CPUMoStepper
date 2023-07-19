import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

while True:
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage: {cpu_usage}%")
    time.sleep(5)