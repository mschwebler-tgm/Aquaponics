#include <RemoteSwitch.h>
#include <OpenAquarium.h>
#include <OneWire.h>
#include <DS1307.h>
#include <DallasTemperature.h>
#include <filter.h>
#include <RemoteReceiver.h>
#include <RTClib.h>

#include <Wire.h>

/*
 *  OpenAquarium sensor platform for Arduino from Cooking-hacks.
 *
 *  Description: Open Aquarium platform for Arduino control several
 *  parameters in order to make a standalone aquarium. Sensors gather     
 *  information and correct possible errors with different actuators.  
 *
 *  In this example we use a DS18B20 to read  temperature. 
 *  It returns a float value of the temperature in ºC.
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

float temperature;

void setup() {
  OpenAquarium.init();   //Initialize
  Serial.begin(115200);
}

void loop() {

  temperature = OpenAquarium.readtemperature(); //Read the sensor
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println("'C");
  delay(2000); //Wait 2 seconds

}
