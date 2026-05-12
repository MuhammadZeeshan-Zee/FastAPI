from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name:str
    age:int

app=FastAPI()

users: List[User]=[]

@app.get("/")
def home():
    return {"message":"welcome to home page"}

@app.get("/user")
def get_all_user():
    return users

@app.post("/user")
def create_user(user:User):
    users.append(user)
    return {"message":"user created successfully"}

@app.get("/user/{id}")
def get_user(id:int):
    return users[id]

@app.put("/user/{id}")
def update_user(id:int, user: User):
    users[id]=user
    return user
    
@app.delete("/user/{id}")
def delete_user(id:int):
    users.pop(id)
    return users
