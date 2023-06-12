# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 27; green = 17; blue = 22 # Ground 역할(green, blue 가 반대로 연결된다.)


GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True) # 여기까지 초기화


try:
    while True:
        GPIO.output(red, False) # 현실에서는 Red가 on 됨
        GPIO.output(green, True)
        GPIO.output(blue, True)
        time.sleep(1)
        GPIO.output(red, True)
        GPIO.output(green, False) # 현실에서는 green이 on 됨
        GPIO.output(blue, True)
        time.sleep(1)
        GPIO.output(red, True)
        GPIO.output(green, True)
        GPIO.output(blue, GPIO.LOW)# 현실에서는 blue가 on 됨
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(blue, GPIO.HIGH)
    GPIO.cleanup()