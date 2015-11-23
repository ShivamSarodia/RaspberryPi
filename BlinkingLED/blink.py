import RPi.GPIO as GPIO
import time

pins = [7, 11]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)

while True:
    time.sleep(0.5)
    GPIO.output(pins, 1)
    time.sleep(0.5)
    GPIO.output(pins, 0)
