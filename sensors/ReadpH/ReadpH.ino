/*
 *  OpenAquarium sensor platform for Arduino from Cooking-hacks.
 *
 *  Description: Open Aquarium platform for Arduino control several
 *  parameters in order to make a standalone aquarium. Sensors gather     
 *  information and correct possible errors with different actuators.
 *
 *  In this example we use a pH probe. It returns an integer value
 *  proportional to the pH level in the water.
 *
 *  Copyright (C) 2012 Libelium Comunicaciones Distribuidas S.L.
 *  http://www.libelium.com
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 *  Version:           0.1
 *  Design:            David Gascon 
 *  Implementation:    Marcos Martinez, Luis Martin & Jorge Casanova
 */

#include "OpenAquarium.h"
#include "Wire.h"

#define calibration_point_4 2221  //Write here your measured value in mV of pH 4
#define calibration_point_7 2104  //Write here your measured value in mV of pH 7
#define calibration_point_10 2031 //Write here your measured value in mV of pH 10


void setup() {
  Serial.begin(115200);
  OpenAquarium.init();
  OpenAquarium.calibratepH(calibration_point_4,calibration_point_7,calibration_point_10);
  delay(1000);
}

void loop() {

  int mvpH = OpenAquarium.readpH(); //Value in mV of pH
  Serial.print(F("pH Value in mV = "));
  Serial.print(mvpH);

  Serial.print(F(" // pH = "));
  float pH = OpenAquarium.pHConversion(mvpH); //Calculate pH value
  Serial.println(pH);

  delay(2000);  //Wait two seconds
}
