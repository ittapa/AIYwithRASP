#library add
import tkinter

import RPi.GPIO as GPIO

#트킨터 객체 생성
root = tkinter.Tk()

#레이블 생성
label = tkinter.Label(root, text="Hello World")

#레이블 배치
label.pack()

#트킨터 객체 표시
root.mainloop()
