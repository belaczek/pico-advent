from machine import ADC, Pin, PWM
from time import sleep

# Set up PIR pin with pull down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the LED pins
amber = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

buzzer = PWM(Pin(13))

print("PIR sensor warming up")
sleep(10)
print("PIR sensor active")


def buzz():
    buzzer.freq(440)
    buzzer.duty_u16(300)
    red.on()
    sleep(1)
    buzzer.duty_u16(0)
    red.off()


def alarm():
    for i in range(5):
        buzz()
        sleep(0.5)


while True:
    sleep(0.01)
    if pir.value() == 1:
        print("Motion detected")
        alarm()
        # sleep(5)
        print("sensor active")
