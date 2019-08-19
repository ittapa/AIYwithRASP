#improt GpIO 라이브러리
import RPi.GPIO as GPIO

import time

#tkinter 라이브러리 
import tkinter

GPIO.setmode(GPIO.BOARD)

ledPin =12

GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)

#TK 객체 인스턴스 선언 root
root = tkinter.Tk()

#root에 표시할 레이블 정의
label = tkinter.Label(root, text='press btn')



#led onoff 함수선언
def ledOn(): GPIO.output(ledPin,GPIO.HIGH)
def ledOff(): GPIO.output(ledPin,GPIO.LOW)

#버튼생성
button1 = tkinter.Button(root, text='on', command=ledOn)
button2 = tkinter.Button(root, text='off', command=ledOff)

#람다
#button1 = tkinter.Button(root, text='on', command=lambda : GPIO.output(ledPin,GPIO.HIGH))
#button2 = tkinter.Button(root, text='off', command=lambda : GPIO.output(ledPin,GPIO.LOW))


#레이블 배치

label.pack()

#버튼 배치
button1.pack()
button2.pack()

#root 생성 표시
root.mainloop()

#GPIO 개방
GPIO.cleanup()