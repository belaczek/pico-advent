from machine import Pin
import time

# Set up tilt sensor pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

counter = 0
state = 0  # 0 = not broken, 1 = broken
startTime = time.time()
currentTime = time.time()
durationSec = 10

while currentTime - startTime < durationSec:
    time.sleep(0.0001)
    currentTime = time.time()

    if beam.value() == 1 and state == 0:
        counter += 1
        state = 1
        print(counter)
    elif beam.value() == 0:
        state = 0

print("Final score: ", counter)
