from machine import Pin, ADC, PWM
from time import sleep
import random

red = Pin(20, Pin.OUT)
green = Pin(19, Pin.OUT)
yellow = Pin(18, Pin.OUT)
# yellow = PWM(Pin(18))
# yellow.freq(1000)

potentiometer = ADC(Pin(27))

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))  # Set the buzzer to PWM mode

A = 440
As = 466
B = 494
C = 523
Cs = 554
D = 587
Ds = 622
E = 659
F = 698
Fs = 740
G = 784
Gs = 830

buzzer.duty_u16(500)


# function which lights up the LED based on the reading
# if the reading is divisible by 2, light up the red LED
# if the reading is divisible by 3, light up the green LED
# if the reading is divisible by 6, light up the yellow LED
def light_led(reading):
    if reading % 12 == 0:
        red.value(1)
    else:
        red.value(0)
    if reading % 21 == 0:
        green.value(1)
    else:
        green.value(0)
    if reading % 10 == 0:
        yellow.on()
    else:
        yellow.off()


# for freq in freqs:
#     buzzer.freq(freq)
#     sleep(0.2)


# Duty to 0 to turn the buzzer off

reading = 0

while True:
    try:
        print(potentiometer.read_u16())
        reading = int(
            potentiometer.read_u16() / 10
            if potentiometer.read_u16() / 10 > 500
            else 500
        )
        buzzer.duty_u16(100)
        buzzer.freq(reading)
        light_led(reading)
        sleep(0.01)
    except KeyboardInterrupt:
        buzzer.duty_u16(0)
        break

buzzer.duty_u16(0)
red.off()
green.off()
yellow.off()

# def playNote(note, volume=500, duration=0.2, delay=0):
#     buzzer.freq(note)
#     buzzer.duty_u16(volume)
#     sleep(duration)
#     buzzer.duty_u16(0)
#     sleep(delay)


# def mute():
#     buzzer.duty_u16(0)


# playNote(C)
# playNote(Cs)
# playNote(D)
# playNote(E)
# playNote(F)
# playNote(G)
# playNote(A)
# playNote(B)

# mute()
