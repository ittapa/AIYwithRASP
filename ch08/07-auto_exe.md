## 부팅시 자동실행

## 편집
    sudo nano /etc/rc.local
    
    
    exit 0 전줄에 코드 삽입
    
    sleep 10 && 
    cd /home/pi/assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/grpc &&
    source /home/pi/env/bin/activate &&
    python3 /home/pi/assistant-sdk-python//google-assistant-sdk/googlesamples/assistant/grpc/pushtotalk_edit.py --lang ko-kr &&
