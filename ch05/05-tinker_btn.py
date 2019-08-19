import tkinter
import RPi.GPIO as GPIO

root = tkinter.Tk()

def printP():
    print ("push")

#버튼 생성
button = tkinter.Button(root, text="Push", command=printP)

#버튼 배치
button.pack()

#root 표시
root.mainloop()


