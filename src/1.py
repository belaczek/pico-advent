from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)
led.toggle()

print("This is my piko blinkink")

# for i in range(10):
#     led.toggle()
#     sleep(0.5)
