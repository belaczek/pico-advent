from machine import Pin
from time import sleep
import random

red = Pin(20, Pin.OUT)
green = Pin(19, Pin.OUT)
yellow = Pin(18, Pin.OUT)

lights = [red, green, yellow]
index = 0

counter = 1

while counter < 100:
    try:
        # lights[index].on()
        # sleep(0.1)
        # lights[index].off()
        # index = (index + 1) % 3
        # counter += 1
        red.value(random.randint(0, 1))
        green.value(random.randint(0, 1))
        yellow.value(random.randint(0, 1))
        sleep(0.2)
    except KeyboardInterrupt:
        break

red.off()
green.off()
yellow.off()
