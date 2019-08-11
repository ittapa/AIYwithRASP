#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>

int fq[]= {262,294,330,349,391,440,494,523};
int main(){
    wiringPiSetup();
    int buzPin = 6;
    
    

    softToneCreate(buzPin);

    for(int i=0; i<8; i++){
        softToneWrite(buzPin, fq[i]);
        delay(300);
    }


    return 0;
}
