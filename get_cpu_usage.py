import psutil
import time
import serial

def get_cpu_usage():
    return int(psutil.cpu_percent(interval=1))

ardport = serial.Serial("/dev/cu.usbmodem11301", 38400)

while True:
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage: {cpu_usage}%")
    ardport.write(str(cpu_usage).encode())
    time.sleep(5)