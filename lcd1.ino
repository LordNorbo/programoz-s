#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2); //példányosítás

void setup() {
  // put your setup code here, to run once:
lcd.init(); //inicializálás
lcd.backlight(); //háttérvilágítás
lcd.setCursor(0,0); //kurzor beallitasa oszlop,sor
lcd.print("Schweibert"); //kiiras az lcdre
lcd.setCursor(5,1);
lcd.print("Norbert");
delay(4000);
}

void loop() {
  // put your main code here, to run repeatedly:
int i;
lcd.clear();
for(i=0;i<16;i++)
{
  lcd.setCursor(i,0);
  lcd.write(247);
  delay(500);
}
for(i=15;i>=0;i--)
{
  lcd.setCursor(i,1);
  lcd.write(244);
  delay(500);
}
}
