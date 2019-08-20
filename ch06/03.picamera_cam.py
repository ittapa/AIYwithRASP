import time
import picamera

camera = picamera.PiCamera() 

camera.start_preview()

camera.start_recording('/home/pi/Desktop/video.h264')
time.sleep(5)

camera.stop_recording()

camera.stop_preview()