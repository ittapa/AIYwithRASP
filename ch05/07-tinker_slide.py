
#tkinter 라이브러리 
import tkinter


#TK 객체 인스턴스 선언 root
root = tkinter.Tk()

#슬라이더ㄹ 값을 저장할 객체 생성 정수형
val = tkinter.IntVar()

#0으로 설정
val.set(0)

#슬라이드 움직였을때 실행되는 함수 선언
def slideFn(scl):
    label.config(text = "value= %d" % int(scl))

    

# 슬라이드 값을 표기하는 레이블생성
label = tkinter.Label(root, text="value = %d" % val.get())

#label 배치
label.pack()


# 슬라이드 생성
slide = tkinter.Scale(root, label="scale", orient="h", from_=0, to=100, showvalue=False, variable=val, command=slideFn)

#슬라이드 생성
slide.pack()


#root 표시
root.mainloop()


#정지및 개방
ledPMW.stop()
GPIO.cleanup()


