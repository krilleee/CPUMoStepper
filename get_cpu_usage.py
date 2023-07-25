import psutil
import time
import serial

# Change this to degrees on the clock
deg_clock = 270;

# Com port and data rate to Arduino
com_port = serial.Serial("/dev/cu.usbmodem11301", 38400)

def scale_cpu_value(cpu_percent):
    # Convert 0-100% CPU value to a scale degrees on clock
    scaled_value = (cpu_percent / 100) * deg_clock
    return int(scaled_value)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

prev_cpu_value = None
cpu_diff = 0;

# Starts controller, seems to skip first value otherwise
com_port.write(str(0).encode())
time.sleep(1)

while True:
    scaled_cpu_value = scale_cpu_value(get_cpu_usage())
    
    # Print the scaled CPU value (degrees on clock) and the change since the previous measurement and sends first value to Arduino
    if prev_cpu_value is not None:
        cpu_diff = scaled_cpu_value - prev_cpu_value
        print(f"Degrees: {scaled_cpu_value}° Change: {cpu_diff}°")
    else:
        com_port.write(str(scaled_cpu_value).encode())
        print(f"Start Degrees: {scaled_cpu_value}°")
    
    # Send the value to Arduino
    time.sleep(5)
    com_port.write(str(cpu_diff).encode())
    
    prev_cpu_value = scaled_cpu_value