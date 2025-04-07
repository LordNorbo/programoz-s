#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
int DT=3;
int CLK=4;
bool gomb=2;
bool be, oldbe;
int A, oldA;
int B;
int csillag=random(0,16);
int teli=random(0,16);
int ido;
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
pinMode(DT,INPUT);
pinMode(CLK,INPUT);
pinMode(gomb,INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
ido=millis();
lcd.setCursor(csillag,0);
lcd.print("*");
lcd.setCursor(teli,1);
lcd.write(255);

A=digitalRead(CLK);
if(A!=oldA)
{
  B=digitalRead(DT);
  if(A==LOW && B==HIGH)//balra
  {
    lcd.setCursor(teli,1);
    lcd.print(" ");
    if(teli<=0)
    {
      teli=0;
    }
    teli=teli-1;
  }
  if(A==LOW && B==LOW)//jobbra
  {
    
    lcd.setCursor(teli,1);
   teli=teli+1;
   if(teli>=15)
    {
      teli=15;
    }
    lcd.print(" ");
  }
}
oldA=A;

be=digitalRead(gomb);
if(be==0 && be!=oldbe)
{
  if(teli==csillag)
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Time:");
    lcd.setCursor(5,0);
    lcd.write(ido);
    lcd.setCursor(10,0);
    lcd.print("sec");
  }
  if(teli!=csillag)
  {
    lcd.clear();
    lcd.setCursor(3,1);
    lcd.print("Try again!");
  }
}
oldbe=be;
}
