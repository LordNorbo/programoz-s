byte pinLED=3;
byte Gomb=0;
bool be,oldbe, allapot=0;
int fenyero, i;

void setup() {
  // put your setup code here, to run once:
pinMode(pinLED,OUTPUT);
pinMode(Gomb,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
be=digitalRead(Gomb);
if(be==0 && be!=oldbe)
{
  if(allapot==0)
  {
for(i=0;i<255;i++)
{
  fenyero=i;
  analogWrite(pinLED,fenyero);
  delay(20);
}
}
else
{
for(i=255;i>0;i--)
{
  fenyero=i;
  analogWrite(pinLED,fenyero);
  delay(20);
}
}
allapot=!allapot;
}
oldbe=be;
}
