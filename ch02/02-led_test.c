#include <stdio.h>
#include <wiringPi.h>

int main(){

    int ledPin = 1;

	if(wiringPiSetup()==-1) return -1; //wiringPi를 설정하는 함수입니다. 만약 설정되지 않았다면 -1이 리터되어 메인함수가 종료합니다.

	pinMode(1, OUTPUT); 

    digitalWrite(1,1); //led를 켭니다.(1)
    delay(3000);
    digitalWrite(1,LOW); //led를 켭니다.(1)
    delay(3000);

	return 0;



}
