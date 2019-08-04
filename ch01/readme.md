boot 에 ssh 파일 추가 : ssh enabled

----------------------------

라즈베리파이와 노트북 연결
 1) 랜선으로 연결.
 2) 제어판 - 네트워크 및 공유센터 - 어댑터 설정 변경 - wifi설정 - 공유탭 - 다른 네트워크 사용자가 이 컴퓨터의 인터넷 연결을 통해 연결할 수 있도록 허용
 3) teraterm으로 접속

-----------------------------

주소 : raspberrypi.mshome.net
아이디 : pi
비밀번호 : raspberry

-----------------------------

명령어

vnc 설정
 1) raspi-config 명령어 입력
 2) interfacing option - vcn enabled 설정
 
설치 패키지 업데이트
sudo apt-get update
 
한글폰트 설치
sudo apt-get install fonts-unfonts-core

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
      
