from pymongo import MongoClient
from config.config import userdb, passworddb, host, portdb

# MONGO_URI = 'mongodb://jm:15332@localhost:27017'
# MONGO_URI = 'mongodb://localhost:27017/'
MONGO_URI = f"mongodb://" + userdb + ":" + \
    passworddb + "@" + host + ":" + portdb + "?authSource=admin"

dbcon = MongoClient(MONGO_URI)
