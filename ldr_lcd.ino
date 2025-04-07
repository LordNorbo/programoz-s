#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
byte ldr;
int ldrertek;
int fenyero;
void setup() {
  // put your setup code here, to run once:
lcd.init();
lcd.backlight();
Serial.begin(9600);
pinMode(ldr,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
ldrertek=analogRead(ldr);
Serial.println(ldrertek);
fenyero=map(ldrertek,100,900,0,15);

}
