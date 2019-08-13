#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    int trig = 23;
    int echo = 24;
    int start_time, end_time;
    float distance;
    if (wiringPiSetup() == -1)
        exit(1);
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
    while (1)
    {
        digitalWrite(trig, LOW);
        delay(500);

        digitalWrite(trig, HIGH);
        delayMicroseconds(10);
        digitalWrite(trig, LOW);

        while (digitalRead(echo) == 0)
            ;
        start_time = micros();
        
        while (digitalRead(echo) == 1)
            ;
        end_time = micros();
        distance = (end_time - start_time) / 29. / 2.;
        printf("distance %.2f cm\n", distance);
    }
    return 0;
}
