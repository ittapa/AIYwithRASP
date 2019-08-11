#include <stdio.h>
#include <wiringPi.h>

int main(){

  int btnPin = 4;

	if(wiringPiSetup()==-1) return -1; //wiringPi를 설정하는 함수입니다. 만약 설정되지 않았다면 -1이 리터되어 메인함수가 종료합니다.

	pinMode(btnPin, INPUT);

	int btn ;

	while(1){
		btn = digitalRead(btnPin);
		
		if(btn == 1){
			printf("on \n");
		}else{
			printf("off \n");
		}
		
		delay(300);
	}

	return 0;


}
