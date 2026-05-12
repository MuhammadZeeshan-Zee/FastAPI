from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from dotenv import load_dotenv
import os

class User(BaseModel):
    name:str
    age:int

app=FastAPI()
load_dotenv()

DB_URL=os.getenv("DB_URL")
print(DB_URL)
client=AsyncIOMotorClient(DB_URL)
db=client.mydatabase

@app.get("/")
def home():
    return {"message":"welcome to home page"}

@app.get("/user")
async def get_all_user():
    users = await db.user.find().to_list(length=None)
    for user in users:
        user["_id"] = str(user["_id"])
    return users

@app.post("/user")
async def create_user(user:User):
    user_dict=user.dict()
    result=await db.user.insert_one(user_dict)
    return {"message":"user created successfully"}

@app.get("/user/{id}")
async def get_user(id):
    user=await db.user.find_one({"_id":ObjectId(id)})
    if not user:
        return {"message":"user not found"}
    user["_id"] = str(user["_id"])
    return user

@app.put("/user/{id}")
async def update_user(id, user: User):
    user_dict=user.dict()
    result= await db.user.update_one({"_id":ObjectId(id)},{"$set":user_dict})
    print(f"result {result}")
    if result.matched_count == 0:
        return {"message": "user not found"}
    if result.modified_count == 0:
        return {"message": "no changes made"}
    return {"message":"user updated successfully"}
    
@app.delete("/user/{id}")
async def delete_user(id):
    result=await db.user.delete_one({"_id":ObjectId(id)})
    print(f"result {result}")
    if result.deleted_count == 0:
        return {"message": "user not found"}
    return {"message":"user deleted successfully"}

