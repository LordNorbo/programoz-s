#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
byte oo[8] = {
  B01010,
  B01010,
  B01110,
  B10001,
  B10001,
  B10001,
  B01110,
  B00000
};
byte ee[8] = {
  B00010,
  B00100,
  B01110,
  B10001,
  B11111,
  B10000,
  B01111,
  B00000
};
int red = 4;
int green = 7;
int blue = 8;
int pinNTC = A0;
int be;
float R1 = 10000; //az ellenállás osztó másik tagja R1=10kohm
float logR2, R2, T;
//Steinhart-Hart együtthatók:
float A = 0.001129148, B = 0.000234125, C = 0.0000000876741;

void setup() {
  // put your setup code here, to run once:
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(green, OUTPUT);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.createChar(0, oo);
  lcd.createChar(1, ee);
  Serial.begin(9600);
  lcd.setCursor(0, 0);
  lcd.print("H");
  lcd.setCursor(1, 0);
  lcd.write(0);
  lcd.setCursor(2, 0);
  lcd.print("m");
  lcd.setCursor(3, 0);
  lcd.write(1);
  lcd.setCursor(4, 0);
  lcd.print("rs");
  lcd.setCursor(6, 0);
  lcd.write(1);
  lcd.setCursor(7, 0);
  lcd.print("klet:");
}

void loop() {
  // put your main code here, to run repeatedly:
  be = analogRead(pinNTC);
  R2 = R1 * ((float)be / (1023.0 - (float)be)); //NTC ellenállás
  logR2 = log(R2);
  T = (1.0 / (A + B * logR2 + C * logR2 * logR2 * logR2)); //Hőmérséklet Kelvinben
  T = T - 273.15; //Hőmérséklet Celsiusban
  Serial.print("Hőmérséklet: ");
  Serial.print(T);
  Serial.println(" °C"); //alt+248
  delay(500);
  lcd.setCursor(0, 1);
  lcd.print(T);
  lcd.setCursor(6, 1);
  lcd.write(223);
  lcd.setCursor(7, 1);
  lcd.print("C");
  if (T <= 27.0)
  {
    digitalWrite(blue, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(green, LOW);
  }
  if (T > 27.0 && T < 32.0)
  {
    digitalWrite(blue, LOW);
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
  }
  if(T>=32.0)
  {
    digitalWrite(blue, LOW);
    digitalWrite(red, HIGH);
    digitalWrite(green, LOW);
  }
}
