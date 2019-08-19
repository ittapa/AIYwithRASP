import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED=18

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while 1:
        #
        GPIO.output(LED, GPIO.HIGH)

        #0.5초대기
        time.sleep(0.5)

        GPIO.output(LED, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("END")
    pass

#GPIO 개방
GPIO.cleanup()