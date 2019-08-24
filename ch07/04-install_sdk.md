# SDK & 샘플 코드 다운로드

## 링크
      https://developers.google.com/assistant/sdk/guides/service/python/embed/install-sample  
          

## python3 환경 설정
      (Python3 사용권장)    

      sudo apt-get update
      sudo apt-get install python3-dev python3-venv
      python3 -m venv env
      env/bin/python -m pip install --upgrade pip setuptools wheel
      source env/bin/activate
        
          
          
## google Assitant SDK 패키지 가져오기

      sudo apt-get install portaudio19-dev libffi-dev libssl-dev
      
### 최신버전으로 업데이터
      python -m pip install --upgrade google-assistant-sdk[samples]
