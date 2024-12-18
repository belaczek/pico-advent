from machine import Pin
from time import sleep

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

state = 0
counter = 0

while True:
    if tilt.value() == 1 and state == 0:
        counter += 1
        state = 1
        print("Tilt detected. Counter: ", counter)
    if tilt.value() == 0:
        state = 0
    sleep(0.1)
