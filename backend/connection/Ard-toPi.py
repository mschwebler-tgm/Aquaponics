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
    """
    parses data to key and value
    :param data: data to be parsed
    :return: None
    """
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
    controls the PWM pin, to regulate the intensity of the lamp
    standard intensity = 0
    :param lightPWM: pin where the lamp is connected to
    :param duration: duration of exposure in minutes
    :param intensity: light-intensity in percent (0-100)
    :return: None
    """
    lightPWM.ChangeDutyCycle(intensity)
    time.sleep(duration * 60)
    lightPWM.ChangeDutyCycle(0)  # turn off the light


def feed(duration):
    """
    Activates the feeder for a certain amount of time
    Note: Feeder has to be connected to Pin nr. 37 (BOARD) in order to work properly
    :param duration: duration of feeding process in seconds
    :return: None
    """
    GPIO.setup(37, GPIO.OUT)
    time.sleep(float(duration))
    GPIO.setup(37, GPIO.IN)


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

# setup boardnumbering and pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
light = GPIO.PWM(12, 100)
light.start(0)  # start with intensity: 0


def controlActuators(r, p):
    """
    listens vor push-messages from redis and reacts by controlling all actuators
    :param r: redis-object
    :param p: pubsub-object
    :return: None
    """
    for message in p.listen():
        data = str(message['data'])
        # use substring to get data when using python 3 (b'data')
        if data.startswith('LED_R'):
            red = data.split(':')[1]
            r.hset('system', 'LED_R', red)
            os.system('pigs p 21 ' + red)  # 'p 21' -> GPIO 21
        elif data.startswith('LED_G'):
            green = data.split(':')[1]
            r.hset('system', 'LED_G', green)
            os.system('pigs p 20 ' + green)  # 'p 20' -> GPIO 20
        elif data.startswith('LED_B'):
            blue = data.split(':')[1]
            r.hset('system', 'LED_B', blue)
            os.system('pigs p 16 ' + blue)  # 'p 16' -> GPIO 16

        elif data.startswith('drops'):
            drops = float(data.split(':')[1])
            while drops > 9:
                drops -= 9
                ser.write(str(drops))
            ser.write(str(drops))

        elif data.startswith('feed'):
            # 'feed:20-39,5;22-30;5'
            # 20-39     -> time
            # 5         -> how long feeder gives food
            feedData = data.split(':')[1]
            times = feedData.split(';')
            # maximum of 5 different times per day
            for i in range(5):
                if i >= len(times):
                    r.hset('system', 'feedHour' + str(i), None)
                    r.hset('system', 'feedMinute' + str(i), None)
                    r.hset('system', 'feedDuration' + str(i), None)
                else:
                    params = times[i].split(',')  # (20-39, 5)
                    r.hset('system', 'feedHour' + str(i), params[0].split('-')[0])
                    r.hset('system', 'feedMinute' + str(i), params[0].split('-')[1])
                    r.hset('system', 'feedDuration' + str(i), params[1])

        elif data.startswith('light'):
            # 'light:20-39,40,90;22-40,20,100'
            # 20-39 -> time
            # 40    -> for 40 minutes
            # 90    -> 90 percent intensity
            lightData = data.split(':')[1]
            times = lightData.split(';')
            # maximum of 5 different times per day
            for i in range(5):
                if i >= len(times):
                    r.hset('system', 'hour' + str(i), None)
                    r.hset('system', 'minute' + str(i), None)
                    r.hset('system', 'duration' + str(i), None)
                    r.hset('system', 'intensity' + str(i), None)
                else:
                    params = times[i].split(',')  # (20-39, 40, 90)
                    r.hset('system', 'hour' + str(i), params[0].split('-')[0])
                    r.hset('system', 'minute' + str(i), params[0].split('-')[1])
                    r.hset('system', 'duration' + str(i), params[1])
                    r.hset('system', 'intensity' + str(i), params[2])


# start thread
thread.start_new_thread(controlActuators, (r, p))

# init RGB-LED-strip
if r.hget('system', 'LED_R') != None:
    os.system('pigs p 21 ' + str(r.hget('system', 'LED_R')))
else:
    os.system('pigs p 21 0')
if r.hget('system', 'LED_G') != None:
    os.system('pigs p 20 ' + str(r.hget('system', 'LED_G')))
else:
    os.system('pigs p 20 0')
if r.hget('system', 'LED_B') != None:
    os.system('pigs p 16 ' + str(r.hget('system', 'LED_B')))
else:
    os.system('pigs p 16 0')

errors = ''
while True:
    try:
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

        # check if it is time to feed
        now = datetime.datetime.now()
        for i in range(5):
            # check if there is a record
            if r.hget('system', 'feedHour' + str(i)) == "None": break
            # compare current time with time of light
            if r.hget('system', 'feedHour' + str(i)) == str(now.hour) and r.hget('system', 'feedMinute' + str(i)) == str(now.minute):
                thread.start_new_thread(feed, (float(r.hget('system', 'feedDuration' + str(i)))))

        # check if it is time to turn on the light
        for i in range(5):
            # check if there is a record
            if r.hget('system', 'hour' + str(i)) == "None": break
            # compare current time with time of light
            if r.hget('system', 'hour' + str(i)) == str(now.hour) and r.hget('system', 'minute' + str(i)) == str(now.minute):
                thread.start_new_thread(expose, (light, float(r.hget('system', 'duration' + str(i))), float(r.hget('system', 'intensity' + str(i)))))

        # check if pH exceeds boundaries
        if r.hmget('system', 'ph') < r.hget('system', 'min_ph'):
            r.publish('system', 'error:pH value not in boundaries\nshould be above ' + r.hget('system', 'min_ph') + ' but is ' + r.hmget('system', 'ph'))
        elif r.hmget('system', 'ph') > r.hget('system', 'max_ph'):
            r.publish('system', 'error:pH value not in boundaries\nshould be below ' + r.hget('system', 'max_ph') + ' but is ' + r.hmget('system', 'ph'))

    except serial.SerialException as err:
        print("Serial connection broken")
        r.publish('system', 'error:No connection to sensors/actuators')
        continue
    except redis.ConnectionError as err:
        print('Redis server not reachable')
        # r.publish('system', 'error:No connection to local database')
        continue
    except Exception as err:
        print("Unknown exception")
        r.publish('system', 'error:Unknown error\n' + str(err))
        continue
