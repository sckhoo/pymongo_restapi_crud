from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os import environ

load_dotenv()
MDB = environ.get("MDB")
MDB_USER = environ.get("MDB_USER")
MDB_PW = environ.get("MDB_PW")
MDB_DB_INSTANCE = environ.get("MDB_DB_INSTANCE")
MDB_DB_COLLECTION = environ.get("MDB_DB_COLLECTION")

uri = "mongodb+srv://"+MDB_USER+":"+MDB_PW+"@"+MDB+".uflbdbq.mongodb.net/?retryWrites=true&w=majority"

conn = MongoClient(uri, server_api=ServerApi('1'))
db = conn[MDB_DB_INSTANCE]
# Choose the collection to insert the document into
collection = db[MDB_DB_COLLECTION]