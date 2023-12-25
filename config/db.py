from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os import environ

load_dotenv()
MDB = environ.get("MDB")
MDB_USER = environ.get("MDB_USER")
MDB_PW = environ.get("MDB_PW")

uri = "mongodb+srv://"+MDB_USER+":"+MDB_PW+"@"+MDB+".uflbdbq.mongodb.net/?retryWrites=true&w=majority"

conn = MongoClient(uri, server_api=ServerApi('1'))
db = conn["pymongo"]
# Choose the collection to insert the document into
collection = db["users"]