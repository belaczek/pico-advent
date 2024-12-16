import onewire, ds18x20, time
from machine import Pin

# Set up the LED pins
amber = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

# Set the data pin for the sensor
SensorPin = Pin(26, Pin.IN)

# Tell MicroPython we're using a DS18B20 sensor, and which pin it's on
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

# Look for DS18B20 sensors (each contains a unique rom code)
roms = sensor.scan()


def indicateTemp(temp):
    if temp < 20:
        green.on()
        amber.off()
        red.off()
    elif temp >= 20 and temp < 25:
        green.off()
        amber.on()
        red.off()
    else:
        green.off()
        amber.off()
        red.on()


while True:
    try:
        sensor.convert_temp()
        time.sleep(2)
        for rom in roms:
            temp = sensor.read_temp(rom)
            rounded = round(temp, 2)
            print(rounded, "C")
            indicateTemp(rounded)
    except KeyboardInterrupt:
        green.off()
        amber.off()
        red.off()
        break
