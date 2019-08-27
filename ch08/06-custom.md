## pushtotalk.py 수정해보기

## 버튼 제거 클릭제거
    if wait_for_user_trigger:
                #click.pause(info='Press Enter to send a new request...')
                time.sleep(1)
            continue_conversation = assistant.assist()
            
## GPIO 버튼으로 시작
        #click.pause(info='Press Enter to send a new request...')           
        GPIO.setup(23, GPIO.IN)
        GPIO.wait_for_edge(23, GPIO.FALLING)

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
                if(userValue =="메롱"): print("반사")
