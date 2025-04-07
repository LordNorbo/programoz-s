#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
int blue=9;
int pinCLK=11; //A
int pinDT=12; //B
int A, oldA, B, fenyero=0, lepcso=8;
int asd;
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
lcd.setCursor(0,0);
pinMode(blue,OUTPUT);
pinMode(pinCLK,INPUT);
pinMode(pinDT,INPUT);
digitalWrite(blue,fenyero);
oldA=digitalRead(pinCLK);
}

void loop() {
  // put your main code here, to run repeatedly:
A=digitalRead(pinCLK);
if(A!=oldA)//Felfutó és lefutó élnél is észleli a változást
{
  B=digitalRead(pinDT);
  if(A==LOW && B==HIGH)//balra
  {
    fenyero-=lepcso;
    if(fenyero<0)fenyero=0;
  }
  if(A==LOW && B==LOW) //jobbra
  {
    fenyero+=lepcso;
    if(fenyero>255) fenyero=255;
  }
  analogWrite(blue,fenyero);
}
oldA=A;
asd=map(fenyero,0,255,0,10);
lcd.setCursor(0,1);
lcd.print(asd);
lcd.setCursor(0,2);
delay(20);
lcd.clear();
}
