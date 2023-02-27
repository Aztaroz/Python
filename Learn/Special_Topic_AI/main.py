# import machine
# import time
# led = machine.Pin(14, machine.Pin.OUT)
# led.value(1)


# motion = False
#
# def handle_interrupt(pin):
#     global motion
#     motion = True
#     global interrupt_pin
#     interrupt_pin = pin
#
#
# led = machine.Pin(2, machine.Pin.OUT)
# pir = machine.Pin(12, machine.Pin.IN)
#
# pir.irq(trigger=machine.Pin.IRQ_RISING, handler=handle_interrupt)
#
# while True:
#     if motion:
#         print('Motion detected! Interrupt caused by:', interrupt_pin)
#         led.value(1)
#         time.sleep(2)
#         led.value(0)
#         print('Motion stopped!')
#         motion = False
#     time.sleep(2)

from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import dht
import machine

# ESP32 Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# DHT22 Pin
sensorDHT = dht.DHT22(machine.Pin(3))

# Motion detector Pin
ldr = Pin(14,Pin.IN)

sleep(2)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Set Time
rtc = machine.RTC()
rtc.datetime((2023,2,20,1,15,53,0,0))

# Main Loop
while True:
    # Get currnet time
    t = rtc.datetime()
    now = '{:04d}-{:02d}-{:02d} {:02d}:{02d}:{:02}'.format(t[0], t[1], t[2], t[4], t[5], t[6])

    try:
        # Read temperature and humidity
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        print("ldr value = ", ldr.value())

        # if motion detected, display time, temperature and humidity
        if ldr.value() == 1:
            print('Object Detected')
            oled.fill(0)
            oled.text('-'*oled_width, 2, 10)
            oled.text("Temp: " + str(temp) + "C", 2, 30, 1)
            oled.text("Humid: " + str(hum) + "%",2,40,1)
            oled.show()
            sleep(2)

        else:
            # If no motion detected, display nothing
            print('no object detected')
            oled.fill(0)

            # it is important to call show() to make the change visible
            oled.show()
    except OSError as e:
        print('Failed to read sensor.')
        sleep((0.5))