#include <stdio.h>
#include <wiringPi.h>

int main(){

    int ledPin = 1;

	if(wiringPiSetup()==-1) return -1; //wiringPi를 설정하는 함수입니다. 만약 설정되지 않았다면 -1이 리터되어 메인함수가 종료합니다.

	pinMode(ledPin, PWM_OUTPUT); // 핀모드를 설정

    pwmWrite(ledPin, 1024);
    delay(500);

    pwmWrite(ledPin, 512);
    delay(500);

    pwmWrite(ledPin, 256);
    delay(500);

    pwmWrite(ledPin, 128);
    delay(500);

    for(int i=0; i<1024; i++){
        pwmWrite(ledPin, i);
        delay(5);
    }
    for(int i=1024; i>0; i--){
        pwmWrite(ledPin, i);
        delay(5);
    }

	return 0;


}
