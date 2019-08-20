import time
import picamera
import RPi.GPIO as GPIO  # new

btnPin =23

GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(btnPin, GPIO.IN)  # new

camera = picamera.PiCamera() 
camera.start_preview()
GPIO.wait_for_edge(btnPin, GPIO.FALLING)  # new
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

#wait_for_edge
#스위치를 누를 경우 폴링 엣지, 스위치가 떼졌을 때 라이징 엣지