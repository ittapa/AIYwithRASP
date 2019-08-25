## start stop trait 추가

### 링크
    https://developers.google.com/assistant/sdk/reference/traits/startstop


### 코드 추가

    @device_handler.command('action.devices.commands.StartStop')
        def abc (start):
            print("start: ", start)
            if start:
                logging.info('Something happened.')
                GPIO.output(18, 1)
            else:
                logging.info('Something else happened.')
                GPIO.output(18, 0)
