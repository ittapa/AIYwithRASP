# 수업준비 및 셋팅
### teraterm 접속

### vnc viewer 접속

### samba server 접속 \\\\raspberrypi.mshome.net

### 접속 실패시 네트워크 공유 설정 재시도

# 카메라 셋팅 및 활용

- 관련 링크

- http://www.3demp.com/community/boardDetails.php?cbID=236


### 카메라 사용설정
#### 환경설정 camera enabled
    - reboot
    
#### 카메라 포트에 연결


#### 연결확인 명령어
- vcgencmd get_camera

- sudo modprobe bcm2835-v4l2

- ls /dev/video0 -l

- sudo nano /etc/modules
    + bcm2835-v4l2

#### 터미널 명령어를 활용한 카메라 사용(사진촬영)
- raspistill -o image.jpg
- raspistill -vf -w 360, -h 280 -o pic.jpg

- raspistill --help
  + 명령어 지원 옵션 확인하기
  
    -o 파일명 -> 파일명으로 저장
    -t 시간 -> 시간 후에 촬영(단위 ms, 기본 5초)
    -w. -h -> 사진 크기 세팅(w 넓이, h 높이)
    -q -> 사진 파일 품질 조정(0~100)
    -d -> demo 모드
    -k -> keypress 모드(엔터 누르면 촬영)
    -s -> signal 모드(신호가 들어오면 촬영)
    -br -> 밝기 조정(0~100)
    
#### 터미널 명령어를 활용한 카메라 사용(영상촬영)


### 파이썬 라이버러리 picamera 활용하기
- 참고링크
 + https://picamera.readthedocs.io/en/release-1.13/recipes1.html
 + http://www.hardcopyworld.com/gnuboard5/bbs/board.php?bo_table=lecture_rpi&wr_id=11



# 카메라 관련 오픈소스 다운로드 / 설치하기
- 관련 링크
- https://bluexmas.tistory.com/826
- http://www.rasplay.org/?p=7174


# 오디오 마이크 설정
 - 참고링크
  https://developers.google.com/assistant/sdk/guides/library/python/embed/audio
