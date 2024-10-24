import subprocess
import time

import board
import busio
import adafruit_vl53l0x

DISPLAY_THRESHOLD = 600 #cm

def initialize_sensor():
    i2c = busio.I2C(board.SCL, board.SDA)
    return adafruit_vl53l0x.VL53L0X(i2c)

def toggle_display(state):
    if state:
      subprocess.call('XAUTHORITY=~pi/.Xauthority DISPLAY=:0 xset dpms force on', shell=True)
    else:
      subprocess.call('XAUTHORITY=~pi/.Xauthority DISPLAY=:0 xset dpms force off', shell=True)

def main():
    sensor = initialize_sensor()
    current_value = 0
    display_state = False

    while True:
        try:
            new_value = sensor.range
            if new_value != current_value:
                current_value = new_value
                display_on = current_value < DISPLAY_THRESHOLD

                if display_on != display_state:
                    display_state = display_on
                    toggle_display(display_on)
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(10.0)

if __name__ == "__main__":
    main()
