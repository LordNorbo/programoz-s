#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
int blue=9;
int pinCLK=11; //A
int pinDT=12; //B
int A, oldA, B, fenyero=0, lepcso=8;
int asd;
int toltes;
bool gomb=6;
bool be, oldbe;
byte szam1;
byte szam2;
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
pinMode(blue,OUTPUT);
pinMode(pinCLK,INPUT);
pinMode(pinDT,INPUT);
pinMode(gomb,INPUT_PULLUP);
digitalWrite(blue,fenyero);
oldA=digitalRead(pinCLK);
}

void loop() {
  // put your main code here, to run repeatedly:
A=digitalRead(pinCLK);
toltes=map(fenyero,0,255,0,25);
if(A!=oldA)//Felfutó és lefutó élnél is észleli a változást
{
if(A==LOW && B==LOW) //jobbra
  {
    fenyero+=lepcso;
    if(fenyero>255) fenyero=255;
    lcd.setCursor(0,0);
    lcd.print("Set code: ");
    lcd.setCursor(10,0);
    lcd.print(toltes);
  }
}
be=digitalRead(gomb);
if(be==0 && be!=oldbe)
{
  szam1=fenyero;
  lcd.clear();
}
oldbe=be;
}
