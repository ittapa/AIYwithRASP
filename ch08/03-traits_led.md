# Traits 활용

## 링크
      https://developers.google.com/assistant/sdk/guides/service/python/extend/register-device-traits


## action 콘솔 접속
     https://console.actions.google.com/
     
### 디바이스 선택
### onoff 체크 후 저장


### smaple 실행 후 turn on

## 예제 소스 다운로드
      git clone https://github.com/googlesamples/assistant-sdk-python

## 명령어 핸들러 코드 찾기
      cd assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/grpc
      
      nano pushtotalk.py
      
      
## onoff 함수 찾기
      device_handler = device_helpers.DeviceRequestHandler(device_id)
      @device_handler.command('action.devices.commands.OnOff')
      def onoff(on):
          if on:
              logging.info('Turning device on')
          else:
              logging.info('Turning device off')
              
              
## GPIO 제어 코드 추가
      device_handler = device_helpers.DeviceRequestHandler(device_id)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
