from fastapi import APIRouter
from models.user import User
from config.db import collection
from bson import ObjectId
from schemas.user import userEntity, usersEntity

user = APIRouter()

pymongo_exception = {
    "message" : "Pymongo Error"
}

@user.get('/')
async def find_all_users():
    try:
        result = collection.find()
    except:
        result = pymongo_exception
    return usersEntity(result)

@user.post('/')
async def create_user(user: User):
    try:
        result = collection.insert_one(dict(user))
        return userEntity(collection.find({"_id":ObjectId(result.inserted_id)}))
    except:
        return userEntity(pymongo_exception)

@user.get('/{id}')
async def find_one_user(id):
    result = collection.find_one({"_id":ObjectId(id)})
    if result:
        return userEntity(result)
    else:
        return userEntity(pymongo_exception)

@user.put('/{id}')
async def update_user(id, user: User):
    try:
        result = collection.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
        return userEntity(collection.find_one({"_id":ObjectId(id)}))
    except:
        return userEntity(pymongo_exception)
    

@user.delete('/{id}')
async def delete_user(id):
    try:
        userEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))
    except:
        return userEntity(pymongo_exception)