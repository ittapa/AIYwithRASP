# 인증진행

### 인증툴 설치 및 업데이트
      python -m pip install --upgrade google-auth-oauthlib[tool]  


### 인증 생성 (ex)
      google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --save --headless --client-secrets /path/to/client_secret_client-id.json
      
### 인증 생성
      google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \ --save --headless --client-secrets /home/pi/파일명.json
      
      
      
