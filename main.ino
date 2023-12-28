void setup() {
  // Initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  static int counter = 0;

  // Send the counter value
  Serial.println(counter);

  // Increment the counter
  counter++;

  // Wait for a second
  delay(1000);
}
