#include <stdio.h>
#include <wiringPi.h>

int main(){

    int led = 1;

	if(wiringPiSetup()==-1) return -1; //wiringPi를 설정하는 함수입니다. 만약 설정되지 않았다면 -1이 리터되어 메인함수가 종료합니다.

	pinMode(led,OUTPUT); //핀모드를 1번으로 설정합니다

	for(;;) //for문
	{
		digitalWrite(led,1); //led를 켭니다.(1)
		delay(500); //0.5초 지연
		digitalWrite(led,0); //led를 끕니다.(0)
		delay(500); //0.5초 지연
	}
	return 0;
}
