#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
byte red=8;
byte green=9;
byte blue=10;
byte joy=A0;
byte gomb=2;
int joybe, varj;
bool be, oldbe;
byte szin=0;
byte ee[8]={
  B00010,
  B00100,
  B00000,
  B01110,
  B10001,
  B11111,
  B10000,
  B01111
};
byte oo[8]={
  B00000,
  B01010,
  B00000,
  B01110,
  B10001,
  B10001,
  B10001,
  B01110
};


void setup() {
  // put your setup code here, to run once:
pinMode(red, OUTPUT);
pinMode(green,OUTPUT);
pinMode(blue,OUTPUT);
pinMode(joy,INPUT);
pinMode(gomb,INPUT);
lcd.init();
lcd.backlight();
lcd.createChar(0,ee);
lcd.createChar(1,oo);
}

void loop() {
  // put your main code here, to run repeatedly:
joybe=analogRead(joy);
varj=map(joybe,0,1023,200,250);
be=digitalRead(gomb);
delay(10);
if(be==0 && be!=oldbe)//be==0 lenyomták a gombot, be!=oldbe nyomvatartás
{
  szin=szin+1;//szín váltása
  if(szin==3)//szín váltásának újrakezdése
  {
    szin=0;
  }
}
if(szin==0)
{
  lcd.setCursor(0,0);
  lcd.print("k");
  lcd.write((byte)0);
  lcd.print("k  ");
  digitalWrite(blue,HIGH);
  delay(varj);
  digitalWrite(blue,LOW);
  delay(varj);
}
if(szin==1)
{
  lcd.setCursor(0,0);
  lcd.print("z");
  lcd.write((byte)1);
  lcd.print("ld");
  digitalWrite(green,HIGH);
  delay(varj);
  digitalWrite(green,LOW);
  delay(varj);
}
if(szin==2)
{
  lcd.setCursor(0,0);
  lcd.print("piros");
  digitalWrite(red,HIGH);
  delay(varj);
  digitalWrite(red,LOW);
  delay(varj);
}
oldbe=be;
}
