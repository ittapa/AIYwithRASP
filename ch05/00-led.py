import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED=12

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

#각 키워드 출력해보기
print("GPIO.OUT: ", GPIO.OUT)
print("GPIO.HIGH: ", GPIO.HIGH)
print("GPIO.LOW: ", GPIO.LOW)

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