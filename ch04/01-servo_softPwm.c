#include<stdio.h>

#include<wiringPi.h>

#include<softPwm.h>



#define SERVO 5



int main()
{

	if(wiringPiSetup()==-1)return 1;

	softPwmCreate(SERVO,0,200);


    softPwmWrite(SERVO, 15); //0 degree
    delay(500);
	softPwmWrite(SERVO, 24); //90 degree
    delay(500);
	softPwmWrite(SERVO, 5); //-90 degree
    delay(500);
	
	return 0;

}
