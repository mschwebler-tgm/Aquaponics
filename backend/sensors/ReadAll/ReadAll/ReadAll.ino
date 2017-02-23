#include <RemoteSwitch.h>
#include <OpenAquarium.h>
#include <OneWire.h>
#include <DS1307.h>
#include <DallasTemperature.h>
#include <filter.h>
#include <RemoteReceiver.h>
#include <RTClib.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include <Wire.h>

// ph calibration points
#define calibration_point_4 2221  //Write here your measured value in mV of pH 4
#define calibration_point_7 2104  //Write here your measured value in mV of pH 7
#define calibration_point_10 2031 //Write here your measured value in mV of pH 10

// ec calibration points
#define point_1_cond 40000   // Write here your EC calibration value of the solution 1 in µS/cm
#define point_1_cal 40       // Write here your EC value measured in resistance with solution 1
#define point_2_cond 10500   // Write here your EC calibration value of the solution 2 in µS/cm
#define point_2_cal 120      // Write here your EC value measured in resistance with solution 2

float temperature;

void setup() {
  OpenAquarium.init();   //Initialize
  Serial.begin(115200);
  OpenAquarium.calibratepH(calibration_point_4,calibration_point_7,calibration_point_10);
  OpenAquarium.calibrateEC(point_1_cond,point_1_cal,point_2_cond,point_2_cal);
}

void loop() {
  // temperature
  temperature = OpenAquarium.readtemperature(); //Read the sensor
  Serial.print("tp "); // tp... temperature
  Serial.println(temperature);
  
  // ph
  int mvpH = OpenAquarium.readpH(); //Value in mV of pH
  float pH = OpenAquarium.pHConversion(mvpH); //Calculate pH value
  Serial.print("ph ");
  Serial.println(pH);

  // ec
  float resistanceEC = OpenAquarium.readResistanceEC(); //EC Value in resistance
  float EC = OpenAquarium.ECConversion(resistanceEC); //EC Value in µS/cm
  Serial.print("ec ");
  Serial.println(EC);

  delay(1000);

}
