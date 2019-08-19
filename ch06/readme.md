# 수업준비 및 셋팅
### teraterm 접속

### vnc viewer 접속

### samba server 접속 \\raspberrypi.mshome.net

### 접속 실패시 네트워크 공유 설정 재시도

# 카메라 셋팅 및 활용

- 관련 링크
- https://bluexmas.tistory.com/826
- http://www.rasplay.org/?p=7174
- http://www.3demp.com/community/boardDetails.php?cbID=236


### 카메라 사용설정
#### 환경설정 camera enabled

- 연결확인 명령어
- vcgencmd get_camera
- sudo modprobe bcm2835-v4l2
- ls /dev/video0 -l
- sudo nano /etc/modules
    + bcm2835-v4l2

-사진 
- raspistill -o image.jpg
- raspistill -vf -w 360, -h 280 -o pic.jpg

