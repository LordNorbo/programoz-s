#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
byte xtengely=A0;
bool gomb;
bool be, oldbe;
int allapot;
int xposition;
int oldposition;
char* string []={"zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"};
void setup() {
  // put your setup code here, to run once:
pinMode(xtengely,INPUT);
pinMode(gomb,INPUT);
lcd.init();
lcd.backlight();
}

void loop() {
  // put your main code here, to run repeatedly:
allapot=analogRead(xtengely);
be=digitalRead(gomb);
xposition=map(allapot,0,1023,0,16);
if(oldposition!=xposition)
{
  lcd.setCursor(oldposition,0); //régi csillag törlése
lcd.print(" ");
}
lcd.setCursor(xposition,0); //új csillag
lcd.print("*");
if(be==0 && be!=oldbe)
{
  lcd.setCursor(0,1);
  lcd.print("                "); 
  
  lcd.setCursor(0,1);
  lcd.print(string[xposition]);
}
oldposition=xposition;
oldbe=be;
}
