import time
import picamera
import tkinter

def captureFn():
    camera = picamera.PiCamera() 
    camera.start_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    
    camera.stop_preview()
    

root = tkinter.Tk()

button = tkinter.Button(root, text="찰칵", command=captureFn)

button.pack()

root.mainloop()
