#include <stdio.h>
#include <wiringPi.h>

int main(){

    int i;

	if(wiringPiSetup()==-1) return -1; //wiringPi를 설정하는 함수입니다. 만약 설정되지 않았다면 -1이 리터되어 메인함수가 종료합니다.

	pinMode(1,OUTPUT); //핀모드를 29번으로 설정합니다.(BCM으로 21번이 wiringPi에서 29번이므로)

	for(i=0;i<5;i++) //for문을 이용하여 동작을 5번 실행합니다.

	{

		digitalWrite(1,1); //led를 켭니다.(1)

		delay(500); //0.5초 지연

		digitalWrite(1,0); //led를 끕니다.(0)

		delay(500); //0.5초 지연

	}

	return 0;



}
