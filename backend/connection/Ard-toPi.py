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
    data = re.sub("['brn\\\]", "", data)

    # split key and value
    return data.split()


# compile and upload .c file (execute commands from cli)
# TODO

# init serial

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200
)

# get redis
r = redis.StrictRedis(host='localhost', port=6380, db=0)
p = r.pubsub()
p.subscribe('system')

cachingStarted = 0
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
        if len(data) != 15 and len(data) != 16:
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
        r.publish('system', 'newData')



        # control actuators
        # get published config
        message = p.get_message()
        if message:
            if str(message.get('data')).startswith('light'):
                pass
            elif str(message.get('data')).startswith('feeder'):
                pass
    except serial.SerialException as err:
        print("Serial connection interface broken")
        print(err)
        errors += 'No connection to sensors/actuators;'
        continue
    except redis.ConnectionError as err:
        print('Redis server not reachable')
        print(err)
        errors += 'No connection to local database;'
        continue
    except Exception as err:
        print("Unknown exception")
        print(err)
        errors += 'Unknown error: ' + str(err) + ';'
        continue