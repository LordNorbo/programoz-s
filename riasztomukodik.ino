byte HiganyPin=7, LedZold=12, LedPiros=13, GombPin=0, BuzzerPin=4;
bool gomb, oldgomb, higany, eles, riaszt;

void setup() {
  pinMode(HiganyPin,INPUT);
  pinMode(GombPin, INPUT);
  pinMode(LedZold, OUTPUT);
  pinMode(LedPiros, OUTPUT);
  pinMode(BuzzerPin, OUTPUT);
  eles=0;
  riaszt=0;
  digitalWrite(LedZold,HIGH);
}

void loop() {
  gomb=digitalRead(GombPin);
  higany=digitalRead(HiganyPin);
  
  if(gomb==0 && gomb!=oldgomb)
  {
    eles=!eles;
  }
  if(eles==1) // élesítve
  {
    digitalWrite(LedZold,LOW);
    digitalWrite(LedPiros,HIGH);  // piros: éles és riaszt
    if(higany==0) //higany bekapcsol (rövidre zárt)
    {
      tone(BuzzerPin,1000);
      delay(1000);
      tone(BuzzerPin,200);
      delay(800);
      noTone(BuzzerPin);
    }
    else  // villogó piros: éles, de nem riaszt
    {
      digitalWrite(LedPiros,HIGH);
      delay(75);
      digitalWrite(LedPiros,LOW);
      delay(75);
    }
  }
  else  // kikapcsolva
  {
    digitalWrite(LedZold,HIGH);
    digitalWrite(LedPiros,LOW);
  }
  oldgomb=gomb;
}
