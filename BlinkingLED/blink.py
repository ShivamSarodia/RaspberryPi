import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

while True:
    time.sleep(1)
    GPIO.output(12, 1)
    time.sleep(1)
    GPIO.output(12, 0)
