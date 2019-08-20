#영을 하고 일정 시간만큼 sleep() 을 한 뒤 다시 촬영하는 패턴입니다. 이걸 몇 일 동안 반복하도록 놔두면 Time-Lapse 영상이 가능

import time
import picamera


def capture_frame(frame):
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.capture('/home/pi/Desktop/lap/frame%03d.jpg' % frame)

# Capture the images
for frame in range(10):
    # Note the time before the capture
    capture_frame(frame)
    # Wait for the next capture. Note that we take into
    # account the length of time it took to capture the
    # image when calculating the delay
    time.sleep(5)