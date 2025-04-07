int be, pinGomb=0; //több változó egy sorban
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600); //soros sebesség
pinMode(pinGomb,INPUT); // digitális bemenet
}

void loop() {
  // put your main code here, to run repeatedly:
be=digitalRead(pinGomb); //beolvasás változóba
Serial.println(be); // írás a soros monitorra
delay(50);
}
