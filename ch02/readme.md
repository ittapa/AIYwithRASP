#xrdp(원격데스크톱 설치) 
sudo apt-get install xrdp


##samba 서버 설치

sudo apt-get install samba samba-common-bin

sudo smbpasswd -a pi //pi 계정 추가

sudo nano /etc/samba/smb.conf 맨 밑줄에 추가 [pi] path=/home/pi comment=PI SAMBA SERVER valid user = pi path=/home/pi/ read only=no browseable=yes create mask=0777 public=yes guest ok=no

ctrl + o :저장 ctrl + x :종료

윈도우 파일 탐색기 주소창 \raspberrypi.mshome.net 으로 접속

권한설정

테라텀 접속후 sudo chmod 777 /home/pi
