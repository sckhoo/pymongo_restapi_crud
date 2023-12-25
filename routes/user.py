from fastapi import APIRouter
from models.user import User
from config.db import collection
from bson import ObjectId
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(collection.find())

@user.post('/')
async def create_user(user: User):
    collection.insert_one(dict(user))
    return usersEntity(collection.find())

@user.get('/{id}')
async def find_one_user(id):
    return userEntity(collection.find_one({"_id":ObjectId(id)}))

@user.put('/{id}')
async def update_user(id, user: User):
    collection.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
    return userEntity(collection.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return userEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))