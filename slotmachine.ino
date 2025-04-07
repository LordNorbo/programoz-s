#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
bool gomb=0;
bool be, oldbe;
int szam1;
int szam2;
int szam3;
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
lcd.setCursor(0,0);
pinMode(gomb,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
szam1=random(1,10);
szam2=random(1,10);
szam3=random(1,10);
be=digitalRead(gomb);
delay(10);
if(be==0 && be!=oldbe)
{
lcd.setCursor(5,0);
lcd.write(255);
lcd.setCursor(6,0);
lcd.print(szam1);
lcd.setCursor(7,0);
lcd.write(255);
lcd.setCursor(8,0);
lcd.print(szam2);
lcd.setCursor(9,0);
lcd.write(255);
lcd.setCursor(10,0);
lcd.print(szam3);
lcd.setCursor(11,0);
lcd.write(255);
}
oldbe=be;
if(szam1==szam2 && szam2==szam3)
{
  lcd.setCursor(5,1);
  lcd.print("Jackpot!");
}
if(szam1!=szam2 && szam3==szam1)
{
  lcd.setCursor(5,1);
  lcd.print("        ");
}
if(szam1==szam2 && szam2!=szam3)
{
  lcd.setCursor(5,1);
  lcd.print("        ");
}
if(szam2==szam1 && szam1!=szam3)
{
  lcd.setCursor(5,1);
  lcd.print("        ");
}
}
