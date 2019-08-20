#coding: utf-8

import picamera
import tkinter

def cap_img():
	if res.get == 3:
		camera.resolution = (1024, 768)
	elif res.get == 2:
		camera.resolution = (640, 480)
	else:
		camera.resolution = (320, 240)
		
	if eff.get == 3:
		camera.image_effect = effect[2][0]
	elif eff.get == 2:
		camera.image_effect = effect[1][0]
	else:
		camera.image_effect = effect[0][0]
		
	filename = et.get()
	camera.capture(filename + '.jpg')
	label4 = tkinter.Label(root, text='Picture Saved')
	label4.pack()
	
root = tkinter.Tk() #root 윈도우 화면 생성

with picamera.PiCamera() as camera:
	resolution = [('320x240', 1), ('640x480', 2), ('1024x768', 3)]
	effect = [('none', 1), ('oilpaint', 2), ('negative', 3)]
	
	res=tkinter.IntVar()
	res.set(1)
	eff=tkinter.IntVar()
	eff.set(1)
	
	label1 = tkinter.Label(root, text='Resolution') # 레이블
	label1.pack() # 화면에 붙임.

	for text, mode in resolution:
		rb1 = tkinter.Radiobutton(root, text=text, 
				variable=res, value=mode)
		rb1.pack(anchor='w')
		
	label2 = tkinter.Label(root, text='Effect')
	label2.pack()

	for text, mode in effect:
		rb2 = tkinter.Radiobutton(root, text=text, 
				variable=eff, value=mode)
		rb2.pack(anchor='w')
		#radio 버튼생성 주입

	#텍스트 주입
	label3 = tkinter.Label(root, text='Save Filename')
	label3.pack()

	#entry t생성
	et = tkinter.Entry(root)
	et.pack()

	
	btn = tkinter.Button(root, text='Picture', width=10, command=cap_img)
	btn.pack()
	
	root.mainloop()


