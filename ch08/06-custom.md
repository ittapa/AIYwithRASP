## pushtotalk.py 수정해보기

## GPIO 코드 추가
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)


## 콘솔 메시지 및 LED 제어
    self.conversation_stream.start_recording()
    logging.info('요청할 오디오 기록시작')
    GPIO.output(40,1)
    
    logging.info('End of audio request detected.')
    logging.info('기록중지')
    GPIO.output(40,0)
    
    





## 버튼 제거 클릭제거
    if wait_for_user_trigger:
                #click.pause(info='Press Enter to send a new request...')
                time.sleep(1)
            continue_conversation = assistant.assist()


     
## GPIO 버튼으로 시작
        #click.pause(info='Press Enter to send a new request...')           
      
        GPIO.wait_for_edge(16, GPIO.FALLING)


## 트킨터 버튼으로 시작


  

##  음성제거
    # if len(resp.audio_out.audio_data) > 0:
            #     if not self.conversation_stream.playing:
            #         self.conversation_stream.stop_recording()
            #         self.conversation_stream.start_playback()
            #         logging.info('Playing assistant response.')
            #     self.conversation_stream.write(resp.audio_out.audio_data)


## 스피치 텍스트 부분
        if resp.speech_results:
            userValue = ''.join(r.transcript
                                      for r in resp.speech_results)
            logging.info('Transcript of user request: "%s".', userValue)
----------------------------
        if(userValue):
            print(userValue)
            if(userValue =="메롱"): 
                print("반사")
            elif(userValue =="불 켜"):  GPIO.output(12, 1)
               
            elif(userValue =="불 꺼"):   GPIO.output(12, 0)
            
            
            
                
---------------------------------------
    if(userValue):
        print(userValue)
        if(userValue =="메롱"): 
            print("반사")
        elif(userValue =="불 켜"):
            GPIO.output(12, 1)
            respVoice = False
        elif(userValue =="불 꺼"):  
            GPIO.output(12, 0)
            respVoice = False

    if len(resp.audio_out.audio_data) > 0 and respVoice:
