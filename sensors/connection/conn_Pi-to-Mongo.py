from pymongo import MongoClient
import redis
import time

# init mongodb and redis
mongoClient = MongoClient('vps336521.ovh.net', 27017)
r = redis.StrictRedis(host='localhost', port=6380, db=0)

# get database
db = mongoClient.urbangreen

# get collection
collection = db['sensor-data']

# repeat every 10 seconds
while True:
    # create new document
    newData = {
        "temperature": r.hget("system", "temperature"),
        "ph": r.hget("system", "ph"),
        "ec": r.hget("system", "ec")
    }
    collection.insert_one(newData)
    print("Wrote data to database.")
    time.sleep(10)
