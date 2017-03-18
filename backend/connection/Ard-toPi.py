import redis
import serial
import time
import os
import re
import thread
import RPi.GPIO as GPIO
import datetime
import sys

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
    data = re.sub("['brn\\\]", "", data)

    # split key and value
    return data.split()

def expose(lightPWM, duration, intensity):
    """

    """
    lightPWM.ChangeDutyCycle(intensity)
    time.sleep(duration*60)
    lightPWM.ChangeDutyCycle(0) # turn off the light

# init serial
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200
)

# get redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('system')

###################################################
## functions to listen for changes for actuators ##
###################################################
# setup boardnumbering and pin
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
light = GPIO.PWM(12, 100)
light.start(0)	# start with intensity: 0

def controlActuators(r, p):
    for message in p.listen():
        data = str(message['data'])
        # use substring to get data when using python 3 (b'data')
	if data.startswith('newData'):
	    continue
        elif data.startswith('LED_R'):
            red = data.split(':')[1]
            r.hset('system', 'LED_R:', red)
            os.system('pigs p 21 ' + red)   # 'p 21' -> GPIO 21
        elif data.startswith('LED_G'):
            green = data.split(':')[1]
            r.hset('system', 'LED_G:', green)
            os.system('pigs p 20 ' + green)  # 'p 20' -> GPIO 20
        elif data.startswith('LED_B'):
            blue = data.split(':')[1]
            r.hset('system', 'LED_B:', blue)
            os.system('pigs p 16 ' + blue)  # 'p 16' -> GPIO 16

        elif data.startswith('drops'):
            drops = data.split(':')[1]
            ser.write(drops)

	elif data.startswith('feed'):
	    timeToFeed = data.split(':')[1]
	    # activate pin 8 for certain amount of time
	    GPIO.output(8, GPIO.HIGH)
	    time.sleep(float(timeToFeed))
	    GPIO.output(8, GPIO.LOW)

        elif data.startswith('light'):
            # 'light:20-39,40,90;22-40,20,100'
            # 20-39 -> time
            # 40    -> for 40 minutes
            # 90    -> 90 percent intensity
            lightData = data.split(':')[1]
            times = lightData.split(';')
            for i in range(5):
                if i >= len(times):
                    r.hset('system', 'hour' + str(i), None)
                    r.hset('system', 'minute' + str(i), None)
                    r.hset('system', 'duration' + str(i), None)
                    r.hset('system', 'intensity' + str(i), None)
                else:
                    params = times[i].split(',') # (20-39, 40, 90)
                    r.hset('system', 'hour' + str(i), params[0].split('-')[0])
                    r.hset('system', 'minute' + str(i), params[0].split('-')[1])
                    r.hset('system', 'duration' + str(i), params[1])
                    r.hset('system', 'intensity' + str(i), params[2])


# start thread
thread.start_new_thread(controlActuators, (r, p))

# init RGB-LED-strip
if r.hget('system', 'LED_R') != None: os.system('pigs p 21 ' + str(r.hget('system', 'LED_R')))
if r.hget('system', 'LED_G') != None: os.system('pigs p 20 ' + str(r.hget('system', 'LED_G')))
if r.hget('system', 'LED_B') != None: os.system('pigs p 16 ' + str(r.hget('system', 'LED_B')))

errors = ''
while True:
    try:
        # save new errors to redis
        r.hset('system', 'error', errors)
        errors = ''

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
        r.hmset(timestamp, {kv_1[0]: kv_1[1], kv_2[0]: kv_2[1], kv_3[0]: kv_3[1]})
        r.publish('system', str(timestamp))

        # check if it is time to turn on the light
        now = datetime.datetime.now()
        for i in range(5):
            # check if there is a record
            if r.hget('system', 'hour'+str(i)) == "None": break
            # compare current time with time of light
            if r.hget('system', 'hour'+str(i)) == str(now.hour) and r.hget('system', 'minute'+str(i)) == str(now.minute):
                thread.start_new_thread(expose, (light, float(r.hget('system', 'duration'+str(i))), float(r.hget('system', 'intensity'+str(i)))))
    except serial.SerialException as err:
        print("Serial connection broken")
        errors += str(timestamp) + ': No connection to sensors/actuators;'
        continue
    except redis.ConnectionError as err:
        print('Redis server not reachable')
        errors += str(timestamp) + ': No connection to local database;'
        continue
    except Exception as err:
        print("Unknown exception")
        errors += str(timestamp) + ': Unknown error: ' + str(err) + ';'
        continue
    except:
        # GPIO.cleanup()
        # do not clean up, as the lamp will continue to shine
        sys.exit()
