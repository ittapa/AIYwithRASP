import time
import picamera
import RPi.GPIO as GPIO

btnPin =23

GPIO.setmode(GPIO.BCM)
GPIO.setup(btnPin, GPIO.IN)

camera = picamera.PiCamera() 

camera.start_preview()

GPIO.wait_for_edge(btnPin, GPIO.FALLING)
camera.start_recording('/home/pi/Desktop/video.h264')
time.sleep(1)

GPIO.wait_for_edge(btnPin, GPIO.FALLING)
camera.stop_recording()

camera.stop_preview()