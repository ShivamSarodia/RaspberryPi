import RPi.GPIO as GPIO
import time

pins = [7, 11]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)

while True:
    time.sleep(1)
    for pin in pins:
        GPIO.output(pin, 1)
    time.sleep(1)
    for pin in pins:
        GPIO.output(pin, 0)
