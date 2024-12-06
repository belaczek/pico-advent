from machine import Pin, ADC, PWM
from time import sleep
import random

red = Pin(20, Pin.OUT)
green = Pin(19, Pin.OUT)
# yellow = Pin(18, Pin.OUT)
yellow = PWM(Pin(18))
yellow.freq(1000)

potentiometer = ADC(Pin(27))

reading = 0

while True:
    print(potentiometer.read_u16())
    reading = potentiometer.read_u16()
    yellow.duty_u16(reading)
    sleep(0.001)


def read_potentiometer():
    reading = potentiometer.read_u16()
    return reading
