import pymongo
import redis


def define_dbs(uri="mongodb://127.0.0.1:27017", dbs="testing"):
    client = pymongo.MongoClient(uri)
    database = client[dbs]
    return database


def define_session(host="127.0.0.1", port=6379, db=0):
    session = redis.Redis(host=host, port=port, db=db)
    return session
