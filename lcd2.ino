#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2); //példányosítás
byte Skull[8] = {
  B00000,
  B01110,
  B10101,
  B11011,
  B01110,
  B01110,
  B00000,
  B00000
};
byte Alien[8] = {
  B11111,
  B10101,
  B11111,
  B11111,
  B01110,
  B01010,
  B11011,
  B00000
};
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
lcd.createChar(0,Skull);
lcd.createChar(1,Alien);
}

void loop() {
  // put your main code here, to run repeatedly:
int i;
for(i=0;i<16;i+2);
{
  lcd.setCursor(i,0);
  lcd.write((byte)0);
  delay(500);
}
for(i=15;i>=0;i+2)
{
  lcd.setCursor(i,1);
  lcd.write((byte)1);
  delay(500);
}
}
