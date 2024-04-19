from pymongo import MongoClient
from config.config import userdb, passworddb, host, portdb

# MONGO_URI = 'mongodb://jm:15332@localhost:27017'
MONGO_URI = f"mongodb://" + userdb + ":" + \
    passworddb + "@" + host + ":" + portdb

dbcon = MongoClient(MONGO_URI)
