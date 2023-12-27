#include <Servo.h>

Servo motor;

void setup() {
  Serial.begin(9600);
  motor.attach(9); // Attach the motor to pin 9
}

void loop() {
  if (Serial.available() > 0) {
    int speed = Serial.parseInt(); // Read the speed value sent from the Raspberry Pi
    if (speed >= 0 && speed <= 180) {
      motor.write(speed); // Set the motor speed
    }
  }
}
