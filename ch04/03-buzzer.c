#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>

int fq[]= {262,294,330,349,391,440,494,523};
int fq2[]= {392,392,440,440,392,392,330,
            392,392,330,330,294,
            392,392,440,440,392,392,330,
            392,330,294,330,262};

int main(){
    wiringPiSetup();
    int buzPin = 6;
    

    softToneCreate(buzPin);

    for(int i=0; i<8; i++){
        softToneWrite(buzPin, fq[i]);
        delay(300);
    }

    // for(int i=0; i<sizeof(fq2) / sizeof(int); i++){
    //     softToneWrite(buzPin, fq2[i]);
    //     delay(500);
    //     softToneWrite(buzPin, 0);
    //     delay(200);
    // }

    return 0;
}
