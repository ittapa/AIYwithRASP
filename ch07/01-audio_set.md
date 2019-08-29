# Google Assistant SDK 설치 


### 오디오 설정
  ## 마이크 연결 확인 (넘버 확인)
     arecord -l
    
  ## 스피커 연결 확인 (넘버확인)
     aplay -l
    
  ## 설정 파일 생성 (경로: /home/pi)
    sudo nano .asoundrc

    
    pcm.!default {
      type asym
      capture.pcm "mic"
      playback.pcm "speaker"
    }
    pcm.mic {
      type plug
      slave {
        pcm "hw:<card number>,<device number>"
      }
    }
    pcm.speaker {
      type plug
      slave {
        pcm "hw:<card number>,<device number>"
        rete 16000
      }
    }
    
  ## 소리 볼륨
      alsamixer
     
  ## 스피커 테스트
      speaker-test -t wav
     
  ## 마이크 테스트
      arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
     
      aplay --format=S16_LE --rate=16000 out.raw
     
     
