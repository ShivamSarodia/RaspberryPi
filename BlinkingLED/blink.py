import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(1, GPIO.OUT)
GPIO.output(1, 1)
