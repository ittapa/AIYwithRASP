설정확인

teraterm 접속

vnc viewer 접속

samba server 접속 \\\raspberrypi.mshome.net

--------------------------------------------
회로도1 LED + BTN


블럭식코딩으로 해보기(스크래치)
led 대신 dc모터 연결해보기)
btn 대신 인체감지 센서 활용 https://www.diymaker.net/113
pwm servo 모터 제어

buzzer 제어

---------------------------------------
PYTHON 코드 작성 -https://studymake.tistory.com/498 
-python3 
import Rpi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(12, GPIO.HIGH)
GPIO.output(12, GPIO.LOW)



LED on / off 반복 코드 작성

BTN code 작성

BTN 활용한 LED 제어 코드 작성

python GUI 툴킷
http://pythonstudy.xyz/python/article/120-Tkinter-%EC%86%8C%EA%B0%9C
