from machine import ADC
import time

# Initialize ADC for temperature sensor
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    try:
        # Read raw ADC value
        reading = sensor_temp.read_u16()

        # Convert raw value to voltage
        voltage = reading * conversion_factor

        # Convert voltage to temperature in Celsius
        temperature = 27 - (voltage - 0.706) / 0.001721

        print("Temperature: {:.2f}°C".format(temperature))

        # Wait for a second before reading again
        time.sleep(1)
    except KeyboardInterrupt:
        break
