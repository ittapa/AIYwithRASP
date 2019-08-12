#include<stdio.h>

#include<wiringPi.h>

#include<softPwm.h>



#define SERVO 5



int main()

{

	char str;



	if(wiringPiSetup()==-1)

		return 1;



	softPwmCreate(SERVO,0,200);

	

	while(1)

	{

		fputs("select c ,r , l , q : " , stdout);

		scanf("%c" , &str);

		getchar();

		if(str=='c') softPwmWrite(SERVO,15); 	 //0 degree

		else if(str=='r') softPwmWrite(SERVO,24); //90 degree

		else if(str=='l') softPwmWrite(SERVO,5); //-90 degree

		else if(str=='q') return 0;

	}	

	

	return 0;

}
