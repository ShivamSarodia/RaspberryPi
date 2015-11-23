import RPi.GPIO as GPIO
import time

pins = [7]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins[0], GPIO.OUT)

while True:
    time.sleep(1)
    GPIO.output(pins[0], 1)
    time.sleep(1)
    GPIO.output(pins[0], 0)
