from machine import ADC, Pin

# Set up the LED pins
amber = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

lightsensor = ADC(Pin(26))


# lightpercent = round(reading / 65535 * 100, 1)

# print("Light level: {}%".format(lightpercent))

reading = 0


while True:
    try:
        reading = lightsensor.read_u16()
        lightpercent = round(reading / 65535 * 100)
        print("Light level: {}%".format(lightpercent))

        if lightpercent < 10:
            red.on()
            amber.off()
            green.off()
            # print("Red")
        elif lightpercent < 50:
            red.off()
            amber.on()
            green.off()
            # print("Amber")
        else:
            red.off()
            amber.off()
            green.on()
            # print("Green")
    except KeyboardInterrupt:
        red.off()
        amber.off()
        green.off()
        break
