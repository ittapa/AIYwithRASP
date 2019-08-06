다운로드 및 설치
1) 라즈비안 os 이미지 다운로드 
- https://www.raspberrypi.org/downloads/raspbian/ - 
- Raspbian Buster with desktop and recommended software
2) win32 disk imager 다운로드 설치
-https://sourceforge.net/projects/win32diskimager/
3) teraterm 다운로드 설치
- https://osdn.net/projects/ttssh2/releases/
- teraterm-4.103.exe
4) vnc viewer 다운로드 설치
- https://www.realvnc.com/en/connect/download/viewer/windows/

라즈비안 os 포팅
- win32diskimager 프로그램 실행
- sd카드 삽입후 해당 드라이브 체크 및 설정
- 라즈비안 os 이미지 설정
- write
- 완료 후 내컴퓨터 열어서 boot 에 ssh 빈파일 추가 : ssh enabled

----------------------------

라즈베리파이와 노트북 공유 및 연결 설정
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


      
