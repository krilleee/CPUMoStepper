import psutil
import time
import serial

def scale_cpu_value(cpu_percent):
    # Convert 0-100% CPU value to a scale from 0-90
    scaled_value = (cpu_percent / 100) * 90
    return int(scaled_value)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)
    
ardport = serial.Serial("/dev/cu.usbmodem11301", 38400)

prev_cpu_value = None
cpu_diff = 0;
# Start controller seems to skip first value otherwise
ardport.write(str(0).encode())
time.sleep(1)


while True:
    cpu_usage = get_cpu_usage()
    scaled_cpu_value = scale_cpu_value(cpu_usage)
    
    # Print the scaled CPU value and the absolute change since the previous measurement
    if prev_cpu_value is not None:
        cpu_diff = scaled_cpu_value - prev_cpu_value
        print(f"CPU Usage: {scaled_cpu_value}% Change: {cpu_diff}%")
    else:
        print(f"CPU Usage: {scaled_cpu_value}%")
        ardport.write(str(scaled_cpu_value).encode())
        print(scaled_cpu_value) # Test
    
    # Send the value to Arduino
    time.sleep(5)
    ardport.write(str(cpu_diff).encode())
    print(cpu_diff) # Test
    
    prev_cpu_value = scaled_cpu_value