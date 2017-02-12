import redis
import serial
import time

# init serial
# TODO 'ttyACM0' needs to be changed to whatever the raspberry Pi's USB-port is called
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200
)

# init redis
r = redis.StrictRedis(host='localhost', port=6380, db=0)

data = ""
while True:
    bytesToRead = ser.inWaiting()
    data = ser.read(bytesToRead)
    if data != "":
        kv = data.split(' ',data)   # kv... KeyValue
        r.hset('system', kv[0], kv[1])   # write data to redis
    time.sleep(0.1)

