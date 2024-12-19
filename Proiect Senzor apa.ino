#define sensorPower 2
#define sensorPin A0

// Valoare pentru stocarea nivelului apei
int val = 0;

void setup() {
  // Setează pinul D7 ca OUTPUT
  pinMode(sensorPower, OUTPUT);
  
  // Setează LOW pentru a nu trece curent prin senzor
  digitalWrite(sensorPower, LOW);
  
  // Inițializează comunicarea serială intre placa si computer
  Serial.begin(9600);
}

void loop() {
  // Obține citirea din funcția de mai jos și o afișează
  int level = readSensor();
  
  Serial.println(level); // Afișează valoarea citită
  
  delay(200); // Așteaptă 200 milisecunde 
}

// Aceasta este o funcție folosită pentru a obține citirea
int readSensor() {
  digitalWrite(sensorPower, HIGH);  // Pornește senzorul
  delay(5);              // Așteaptă 5 milisecunde
  val = analogRead(sensorPin);    // Citește valoarea analogică de la senzor
  digitalWrite(sensorPower, LOW);   // Oprește senzorul
  return val;             // Returnează citirea curentă
}
