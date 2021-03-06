import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED=18
BTN=23

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BTN, GPIO.IN)

try:
    while 1:
        
    
        if GPIO.input(BTN) == 0:
            print ("button pressed")
            GPIO.output(LED, True)

        else:
            print ("button not pressed")
            GPIO.output(LED, False)
    
        time.sleep(0.5)

except KeyboardInterrupt:
    print("END")
    pass

GPIO.cleanup()