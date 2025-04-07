#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
bool gomb1=0;
bool gomb2=1;
bool be1, be2, oldbe1, oldbe2;
int i;
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
lcd.setCursor(0,0);
lcd.clear();
pinMode(gomb1,INPUT);
pinMode(gomb2,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
be1=digitalRead(gomb1);
be2=digitalRead(gomb2);
if(be1!=oldbe1&& be1==0)
{
  i=i+1;
  lcd.write(255);
  lcd.setCursor(i,0);
 
}
delay(50);
oldbe1=be1;
if(be2!=oldbe2 && be2==0)
{
  i=i-1;
  lcd.print(" ");
  lcd.setCursor(i,0);
}
delay(50);
oldbe2=be2;
if(i>16)
{
  i=16;
}
  if(i<0)
  {
    i=0;
  }
}
