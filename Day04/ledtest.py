import RPi.GPIO as GPIO
import time
btnPin = 24
count = 0
red = 17
green = 27
blue = 22

def clickHndler(channel):
  global count
  count = count +1
  if (count %2 ==0):
    GPIO.output(red, GPIO.LOW)
  else:
    GPIO.output(red, GPIO.HIGH)
  print(count)
   
GPIO.setwarnings(False) # 쓸데 없는 경고 표시 로그 사라짐
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button, GPIO.RISING, callback=clickhndler)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red,True)
GPIO.output(green,True)
GPIO.output(blue,True) # 여기 까지 초기화