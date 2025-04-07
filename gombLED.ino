bool Gomb, oldGomb, allapot;
byte pinLED=4;
byte pinGomb=0;
void setup() {
  // put your setup code here, to run once:
pinMode(pinGomb,INPUT);
pinMode(pinLED,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
Gomb=digitalRead(pinGomb);
if(Gomb==0 && Gomb!=oldGomb) // a gomb előző állapotának figyelése
{
  allapot=!allapot; // LED állapot átkapcsolása !allapot az negálás
  digitalWrite(pinLED,allapot);
  delay(50);
}
oldGomb=Gomb; // a Gomb előző állapotának tárolása
}
