import redis
import serial
import time
import os
import re


def getKeyValue(data):
    """"""
    """ output when reading continously from serial port:
    b'temperature 24.62\r\n'
    b''
    b''
    b''
    b'ph -30.56\r\n'
    b''
    ...
    """
    # extrude essential data: b'temperature 24.62\r\n'
    #                         -> temperature 24.62
    # data = re.sub("['brn\\\]", "", data)

    # split key and value
    return data.split()


# compile and upload .ino file (execute commands from cli)
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire /tmp/build7502389626690339678.tmp/ReadAll.cpp -o /tmp/build7502389626690339678.tmp/ReadAll.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/OpenAquarium.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/OpenAquarium.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/DallasTemperature.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/DallasTemperature.cpp.o ")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/RTClib.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/RTClib.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/DS1307.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/DS1307.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/OneWire.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/OneWire.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/RemoteSwitch.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/RemoteSwitch.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/RemoteReceiver.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/RemoteReceiver.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/home/pi/sketchbook/libraries/OpenAquarium/utility /home/pi/sketchbook/libraries/OpenAquarium/filter.cpp -o /tmp/build7502389626690339678.tmp/OpenAquarium/filter.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/usr/share/arduino/libraries/Wire/utility /usr/share/arduino/libraries/Wire/Wire.cpp -o /tmp/build7502389626690339678.tmp/Wire/Wire.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard -I/home/pi/sketchbook/libraries/OpenAquarium -I/usr/share/arduino/libraries/Wire -I/usr/share/arduino/libraries/Wire/utility /usr/share/arduino/libraries/Wire/utility/twi.c -o /tmp/build7502389626690339678.tmp/Wire/utility/twi.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/avr-libc/malloc.c -o /tmp/build7502389626690339678.tmp/malloc.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/avr-libc/realloc.c -o /tmp/build7502389626690339678.tmp/realloc.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/wiring_digital.c -o /tmp/build7502389626690339678.tmp/wiring_digital.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/wiring_pulse.c -o /tmp/build7502389626690339678.tmp/wiring_pulse.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/WInterrupts.c -o /tmp/build7502389626690339678.tmp/WInterrupts.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/wiring_analog.c -o /tmp/build7502389626690339678.tmp/wiring_analog.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/wiring_shift.c -o /tmp/build7502389626690339678.tmp/wiring_shift.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -c -g -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/wiring.c -o /tmp/build7502389626690339678.tmp/wiring.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/Tone.cpp -o /tmp/build7502389626690339678.tmp/Tone.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/IPAddress.cpp -o /tmp/build7502389626690339678.tmp/IPAddress.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/new.cpp -o /tmp/build7502389626690339678.tmp/new.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/Stream.cpp -o /tmp/build7502389626690339678.tmp/Stream.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/CDC.cpp -o /tmp/build7502389626690339678.tmp/CDC.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp -o /tmp/build7502389626690339678.tmp/HardwareSerial.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/USBCore.cpp -o /tmp/build7502389626690339678.tmp/USBCore.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/main.cpp -o /tmp/build7502389626690339678.tmp/main.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/WString.cpp -o /tmp/build7502389626690339678.tmp/WString.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/HID.cpp -o /tmp/build7502389626690339678.tmp/HID.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/WMath.cpp -o /tmp/build7502389626690339678.tmp/WMath.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-g++ -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/standard /usr/share/arduino/hardware/arduino/cores/arduino/Print.cpp -o /tmp/build7502389626690339678.tmp/Print.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/malloc.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/realloc.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/wiring_digital.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/wiring_pulse.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/WInterrupts.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/wiring_analog.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/wiring_shift.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/wiring.c.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/Tone.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/IPAddress.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/new.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/Stream.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/CDC.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/HardwareSerial.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/USBCore.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/main.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/WString.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/HID.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/WMath.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-ar rcs /tmp/build7502389626690339678.tmp/core.a /tmp/build7502389626690339678.tmp/Print.cpp.o")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-gcc -Os -Wl,--gc-sections -mmcu=atmega328p -o /tmp/build7502389626690339678.tmp/ReadAll.cpp.elf /tmp/build7502389626690339678.tmp/ReadAll.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/OpenAquarium.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/DallasTemperature.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/RTClib.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/DS1307.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/OneWire.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/RemoteSwitch.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/RemoteReceiver.cpp.o /tmp/build7502389626690339678.tmp/OpenAquarium/filter.cpp.o /tmp/build7502389626690339678.tmp/Wire/Wire.cpp.o /tmp/build7502389626690339678.tmp/Wire/utility/twi.c.o /tmp/build7502389626690339678.tmp/core.a -L/tmp/build7502389626690339678.tmp -lm")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-objcopy -O ihex -j .eeprom --set-section-flags=.eeprom=alloc,load --no-change-warnings --change-section-lma .eeprom=0 /tmp/build7502389626690339678.tmp/ReadAll.cpp.elf /tmp/build7502389626690339678.tmp/ReadAll.cpp.eep")
os.system("/usr/share/arduino/hardware/tools/avr/bin/avr-objcopy -O ihex -R .eeprom /tmp/build7502389626690339678.tmp/ReadAll.cpp.elf /tmp/build7502389626690339678.tmp/ReadAll.cpp.hex")
os.system("/usr/share/arduino/hardware/tools/avrdude -C/usr/share/arduino/hardware/tools/avrdude.conf -v -v -v -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:/tmp/build7502389626690339678.tmp/ReadAll.cpp.hex:i")


try:
    # init serial
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=115200
    )

    # get redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)


    cachingStarted = 0
    while True:
        # read from serial port
        bytesToRead = ser.inWaiting()
        data = str(ser.read(bytesToRead))

        # sync input from serial so that "b'tp 25.50\r\n'" is not split into "b'tp " and "25.50\r\n"
        if len(data) != 10 and len(data) != 11:
            time.sleep(0.1)
            continue

        timestamp = str(int(time.time()))

        # get all 3 kinds of data (temp, ph, ec)
        kv_1 = getKeyValue(data)
        time.sleep(0.1)
        data = str(ser.read(bytesToRead))
        kv_2 = getKeyValue(data)
        time.sleep(0.1)
        data = str(ser.read(bytesToRead))
        kv_3 = getKeyValue(data)

        # save to redisDB with timestamp
	print(timestamp + ": " + kv_1[0] + kv_1[1] + "; " + kv_2[0] + kv_2[1] + "; " + kv_3[0] + kv_3[1])
        r.hmset(timestamp, {kv_1[0]: kv_1[1], kv_2[0]: kv_2[1], kv_3[0]: kv_3[1]})
        r.publish('system', 'newData')
except serial.SerialException as err:
    print("Serial connection interface broken")
    print(err)
    # TODO set error message (redis) 1
except redis.ConnectionError as err:
    print('Redis server not reachable')
    print(err)
    # TODO set error message (redis) 2
except Exception as err:
    print("Unknown exception")
    print(err)
    # TODO set error message (redis) 3
