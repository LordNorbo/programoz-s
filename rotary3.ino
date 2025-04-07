#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
bool gomb=0;
bool be, oldbe;
int pinCLK=11; //A
int pinDT=12; //B
int A, oldA, B, fenyero=0, lepcso=8;
byte i=0;
int asd;
int toltes;
byte koda=0;
byte kodb=0;
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
lcd.setCursor(0,0);
pinMode(pinCLK,INPUT);
pinMode(pinDT,INPUT);
pinMode(gomb,INPUT_PULLUP);
oldA=digitalRead(pinCLK);
}

void loop() {
  // put your main code here, to run repeatedly:
  be=digitalRead(gomb);
A=digitalRead(pinCLK);
if(A!=oldA)//Felfutó és lefutó élnél is észleli a változást
{
  B=digitalRead(pinDT);
  if(A==LOW && B==LOW) //jobbra
  {
    i=i-1;
  }
  if(A==LOW && B==LOW)
  {
    i=i+1;
  }
}

oldA=A;
lcd.setCursor(0,0);
lcd.print(i);
if(i>10)
{
  i=10;
  lcd.clear();
}
if(i==9)
{
  lcd.setCursor(1,0);
  lcd.print(" ");
  lcd.setCursor(0,0);
}
if(i<0)
{
  i=0;
}
if(be==0 && be!=oldbe)
{
  if(koda==0)
  {
    koda=i;
  }
  else
  {
    if(kodb==0)
    {
      kodb=i;
      delay(100);
    }
  }
}
oldbe=be;
if(koda!=0 && kodb!=0)
{
  if(koda==1 && kodb==3)
  {
    lcd.setCursor(0,1);

    lcd.setCursor(0,1);
    lcd.print("OPEN");
  }
  if(koda!=1 || kodb!=3)
  {
    lcd.setCursor(0,1);

    lcd.setCursor(0,1);
    lcd.print("ALARM");
  }
}
}
