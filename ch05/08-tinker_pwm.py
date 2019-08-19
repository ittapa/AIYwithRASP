#improt GpIO 라이브러리
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

ledPin =12

GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)

#pwm 객체선언
ledPWM = GPIO.PWM(ledPin, 500)

ledPWM.start(0)


ledPWM.ChangeDutyCycle(0)
time.sleep(1)
ledPWM.ChangeDutyCycle(50)
time.sleep(1)
ledPWM.ChangeDutyCycle(100)
time.sleep(1)



#정지및 개방
ledPWM.stop()
GPIO.cleanup()


