
#include <SparkFun_ADS1015_Arduino_Library.h> //Bibliothek unter folgendem Link verfügbar:  http://librarymanager/All#SparkFun_ADS1015

#include <Wire.h>
#include "SparkFun_Qwiic_OpenLog_Arduino_Library.h" // OpenLog library

const int sampleRateHz = 700;
unsigned long lastMicros = 0;

void setup() {
  Serial.begin(500000); // High baud rate
}

void loop() {
  unsigned long now = micros();
  if (now - lastMicros >= sampleRateHz) {
    lastMicros += sampleRateHz;

    int val = analogRead(A0);
    Serial.println(val); // Send only the value (or: "millis(),val" for timestamps)
  }
}
