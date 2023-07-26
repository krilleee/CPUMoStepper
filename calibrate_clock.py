import keyboard
import time
import serial

# Com port and data rate to Arduino
com_port = serial.Serial("/dev/cu.usbmodem11301", 38400)

value = 0

def write_str():
    time.sleep(1)
    com_port.write(str(value).encode())

while True:
    try:
        if keyboard.is_pressed('left'):
            value = -1
            print(f"Value decreased to {value}")
            write_str()
        elif keyboard.is_pressed('right'):
            value = 1
            print(f"Value increased to {value}")
            write_str()
        elif keyboard.is_pressed("up"):
            value = 10
            print(f"Value increased by {value}")
            write_str()
        elif keyboard.is_pressed("Down"):
            value = -10
            print(f"Value decreased by {value}")
            write_str()
        elif keyboard.is_pressed('enter'):
            manual_input = input("How many degrees?: ")
            if manual_input.strip():  # Check if the input is not empty
                value = int(manual_input)
                write_str()

    except:
        break