#include <TinyStepper.h>

// Define Arduino Pin Outputs
#define IN1 8
#define IN2 9
#define IN3 10
#define IN4 11
#define HALFSTEPS 4096  // Number of half-steps for a full rotation

// Init the TinyStepper Class
TinyStepper stepper(HALFSTEPS, IN1, IN2, IN3, IN4);

void setup()
{
  Serial.begin(38400);
  stepper.Enable();
  delay(1000);
}

// Receve value from Pyhon program
void loop() {
  if (Serial.available())
  {
    String a = Serial.readString();
    Serial.print("CPU Use %: ");
    Serial.println(a);
    int b = a.toInt();
    stepper.Move(b, OUTPUT);
    delay(2000);
  }
}