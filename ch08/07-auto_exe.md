## 부팅시 자동실행

## start sh 파일 생성
    sudo nano start.sh
    
    #!/bin/bash
##
    sleep 10
    source /home/pi/env/bin/activate 2>&1 | logger -t aistart
    python3 /home/pi/assistant-sdk-python//google-assistant-sdk/googlesamples/assistant/grpc/pushtotalk_edit.py --lang ko-kr 2>&1 | logger -t aistart

    
    
    
## 복사
    sudo cp ./start.sh /etc/profile.d/start.sh
    
## 재부팅
    reboot
    
