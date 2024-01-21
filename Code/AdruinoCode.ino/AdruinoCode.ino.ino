#include <cvzone.h>
#include <Servo.h>
Servo myservo;
SerialData serialData(2, 1);
int valsRec[2]; // array of int with size mrOfVaIsRec

void setup() {
    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);
    serialData. begin();
    myservo.attach(9);
}

void loop() {
    int pos;
    serialData.Get(valsRec) ;
    if(valsRec[0] == 1)
    {
              myservo.write(180);              // tell servo to go to position in variable 'pos'
              digitalWrite(13, HIGH);
              digitalWrite(12, LOW);
              delay(15);                       // waits 15ms for the servo to reach the position
      } 
  else if(valsRec[1] == 0)
    {
        myservo.write(0);              // tell servo to go to position in variable 'pos'
        digitalWrite(13, LOW);
        digitalWrite(12, HIGH);
        delay(15);                       // waits 15ms for the servo to reach the position
    }
}
