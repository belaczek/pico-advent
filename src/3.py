from machine import Pin
from time import sleep
import random

red = Pin(20, Pin.OUT)
green = Pin(19, Pin.OUT)
yellow = Pin(18, Pin.OUT)

# Set up our button name and GPIO pin number
# Also set the pin as an input and use a pull down
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    sleep(0.2)
    # red.value(button1.value())
    # green.value(button2.value())
    # yellow.value(button3.value())
    if button1.value() == 1:
        print("Button 1 pressed")
        red.toggle()
    if button2.value() == 1:
        print("Button 2 pressed")
        green.toggle()
    if button3.value() == 1:
        print("Button 3 pressed")
        yellow.toggle()


# lights = [red, green, yellow]
# index = 0

# counter = 1

# while counter < 100:
#     try:
#         # lights[index].on()
#         # sleep(0.1)
#         # lights[index].off()
#         # index = (index + 1) % 3
#         # counter += 1
#         red.value(random.randint(0, 1))
#         green.value(random.randint(0, 1))
#         yellow.value(random.randint(0, 1))
#         sleep(0.2)
#     except KeyboardInterrupt:
#         break

# red.off()
# green.off()
# yellow.off()
