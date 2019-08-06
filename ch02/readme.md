텍스트 에디터 visual stuideocode 설치
https://code.visualstudio.com/download


xrdp(원격데스크톱 설치)
sudo apt-get install xrdp

samba 서버 설치
 1) sudo apt-get install samba samba-common-bin
 2) sudo smbpasswd -a pi     //pi 계정 추가
 3) sudo nano /etc/samba/smb.conf
    맨 밑줄에 추가
    [pi]
    path=/home/pi
    comment=PI SAMBA SERVER
    valid user = pi
    path=/home/pi/
    read only=no
    browseable=yes
    create mask=0777
    public=yes
    guest ok=no
    
    ctrl + o :저장
    ctrl + x :종료
    
  4) 윈도우 파일 탐색기 주소창 \\raspberrypi.mshome.net 으로 접속
  5) 권한설정
     - 테라텀 접속후
      sudo chmod 777 /home/pi
      
      
wiringPi
      --http://wiringpi.com/reference/setup/
      

gpio
셀 명령어
 --- /usr/bin/gpio
gpio readall
gpio mode 1 out
gpio write 1 1
gpio write 1 0

bcm gpio 핀 번호를 이용한 제어
gpio -g mode 18 out
gpio -g write 18 1
gpio -g write 18 0

