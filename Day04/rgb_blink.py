# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 22
green = 27
blue = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    while True:
        GPIO.output(red, True)
        GPIO.output(blue, False)
        GPIO.output(green, False)

        time.sleep(1)
        GPIO.output(red, False)
        GPIO.output(blue, True)
        GPIO.output(green, False)
        time.sleep(1)
        GPIO.output(red, False)
        GPIO.output(blue, False)
        GPIO.output(green, True)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()