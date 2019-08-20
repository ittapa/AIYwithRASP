#picamera import
import time
import picamera


#PiCamera 객체 선언
camera = picamera.PiCamera()

camera.start_preview()

#각도 변경
#camera.rotation = 90
#size 변경
#camera.resolution = (1024, 512)

#5초 대기
time.sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')

camera.stop_preview()