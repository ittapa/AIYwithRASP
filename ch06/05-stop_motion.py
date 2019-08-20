import picamera
import RPi.GPIO as GPIO


btnPin =23

GPIO.setmode(GPIO.BCM)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
    camera.start_preview()
    frame = 1
    while True:
        GPIO.wait_for_edge(btnPin, GPIO.FALLING)
        camera.capture('/home/pi/Desktop/motion/frame%03d.jpg' % frame)
        frame += 1
    camera.stop_preview()