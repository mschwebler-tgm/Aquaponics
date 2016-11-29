import redis
import serial
import time

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200
)
#    parity=serial.PARITY_ODD,
#    stopbits=serial.STOPBITS_TWO,
#    bytesize=serial.SEVENBITS

print(ser.name)

data = ""
while True:
    bytesToRead = ser.inWaiting()
    data = ser.read(bytesToRead)
    if data != "":
    	print("Data: " + data)
    time.sleep(0.1)


#r = redis.StrictRedis(host='localhost', port=6380, db=0)
#r.hset('system','foo', 'baar')
#r.get('temperature')