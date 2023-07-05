import RPi.GPIO as GPIO

import time 

GPIO.setwarnings(False)         


Ds = 4   #GPIO 4pin - 74ch595 14pin

STCP = 5 #GPIO 5pin - 74ch595 12pin

SHCP = 6 #GPIO 6pin - 74ch595 11pin      


GPIO.setmode (GPIO.BCM)      

GPIO.setup(Ds,GPIO.OUT)         #GPIO 출력설정

GPIO.setup(STCP,GPIO.OUT)

GPIO.setup(SHCP,GPIO.OUT)

# VCC 공통인 anode 세븐 세그먼트는 1이 되면 꺼짐.

# GND 공통인 cathode 세븐 세그먼트는 0이 되면 꺼짐.

# 본 예제는 에노드 타입 입니다.

list =[

    [1,0,0,0,0,0,0,0],   #0

    [1,1,1,1,0,0,1,1],   #1

    [0,1,0,0,1,0,0,1],   #2 

    [0,1,1,0,0,0,0,0],   #3

    [0,0,1,1,0,0,1,1],   #4

    [0,0,1,0,0,1,0,0],   #5

    [0,0,0,0,0,1,0,0],   #6

    [1,0,1,1,0,0,0,0],   #7

    [0,0,0,0,0,0,0,0],   #8

    [0,0,1,0,0,0,0,0],   #9


]


while 1:                               # 무한 반복

    for y in range(10):

        for x in list[y]:

            GPIO.output(SHCP,0)          #SHCP(LATCH) LOW로 변경

            time.sleep(0.001)

            GPIO.output(Ds,x)              # DS(DATA) 데이터 비트 넣기

            GPIO.output(STCP,1)           # STCP(CLOCK) 클럭 핀 HIGH

            time.sleep(0.001)

            GPIO.output(SHCP,1)           # SHCP(LATCH) ON -> 

            time.sleep(0.001)                         #DATA 병렬로 출력

            GPIO.output(STCP,0)           # STCP(CLOCK) 클럭 LOW

            time.sleep(0.001)

            GPIO.output(SHCP,0)          # SHCP(LATCH) OFF -> 출력 안함

            print(x)

        time.sleep(1.5)