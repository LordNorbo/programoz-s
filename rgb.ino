int red=6;
int green=5;
int blue=4;
int be, pinGomb=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(red,OUTPUT);
pinMode(green,OUTPUT);
pinMode(blue,OUTPUT);
pinMode(pinGomb,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
be=digitalRead(pinGomb);
Serial.println(be);
if(be==1)
{
  digitalWrite(red,HIGH);
  digitalWrite(green,LOW);
}
else
{
  digitalWrite(green,HIGH);
  digitalWrite(red,LOW);
}

}
