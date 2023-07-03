import os
import time

import board
import busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

current_value = 0
display_state = False

while True:
    new_value = sensor.range
    if new_value != current_value:
        current_value = new_value
        if current_value < 600:
            display_on = True
        else:
            display_on = False

    if display_on != display_state:
        display_state = display_on
        if display_on:
            os.system("export DISPLAY=:0 && xset dpms force on")
        else:
            os.system("export DISPLAY=:0 && xset dpms force off")

    time.sleep(1.0)
