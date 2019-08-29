# 인증진행

### 인증툴 설치 및 업데이트
      python -m pip install --upgrade google-auth-oauthlib[tool]  


### 인증 생성 (ex)
      google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \ --save --headless --client-secrets /path/to/client_secret_client-id.json
      
### 인증 생성
      google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \ --save --headless --client-secrets /home/pi/파일명.json
      
      
      
### 인증주소 복사 열기
      로그인 
      허용
      코드 복사
      Enter the authorization code:
      붙여넣기 인증
      완료메시지: credentials saved: /path/to/.config/google-oauthlib-tool/credentials.json
      
      
