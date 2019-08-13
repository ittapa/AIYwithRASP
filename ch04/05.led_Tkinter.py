#improt GpIO 라이브러리
import RPi.GPIO as GPIO

import time

#tkinter 라이브러리 
import tkinter

GPIO.setmode(GPIO.BOARD)

ledPin =12

GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)


#led onoff 함수 생성
def ledOnOff():
    print(GPIO.input(ledPin))
    GPIO.output(ledPin, not GPIO.input(ledPin))


#TK 객체 인스턴스 선언 root
root = tkinter.Tk()

#root에 표시할 레이블 정의
label = tkinter.Label(root, text='press btn')

#레이블 배치
label.pack()

#버튼생성
button = tkinter.Button(root, text='led', command=ledOnOff)

#버튼 배치
button.pack()


#root 생성 표시
root.mainloop()

#GPIO 개방
GPIO.cleanup()






