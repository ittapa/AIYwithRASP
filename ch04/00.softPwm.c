#include<stdio.h>
#include<wiringPi.h>
#include<softPwm.h>
 
#define SERVO 1
 
int main() {
        char str;
 
        if(wiringPiSetup()==-1)
                return 1;
 
        softPwmCreate(1 , 0, 200); //0~1024 0 200

        while(1)
        {
                softPwmWrite(1, 0);
                delay(300);
                softPwmWrite(1, 100);  
                delay(300);
                softPwmWrite(1, 200);  
                delay(300);
        }
  
 
        return 0;
}


