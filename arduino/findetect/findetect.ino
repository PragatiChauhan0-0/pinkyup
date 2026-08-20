int LED1 = 13;
int LED2 = 12;
int LED3 = 11;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    // Read the incoming data
    int count = Serial.read() - '0';
    // convert to binary and turn on the corresponding LEDs
    digitalWrite(LED1, count & 1);
    digitalWrite(LED2, count & 2);
    digitalWrite(LED3, count & 4);
  }
}
