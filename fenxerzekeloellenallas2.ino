int led=11;
int ldr=A0;
int ldrertek;
int feny;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led,OUTPUT);
pinMode(ldr,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
ldrertek=analogRead(ldr);
Serial.println(ldrertek);
feny=map(ldrertek,10,1020,0,255); //(elso amit konvertalunk,masodik amirol konvertalunk

if(feny<=100)
{
  analogWrite(feny, led);
}
else
{
  analogWrite(led,LOW);
}
}
