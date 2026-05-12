from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
class Vehical(BaseModel):
    model:str
    company:str

app=FastAPI()

@app.get("/")
def home():
    return {"message":"welcome to home page"}

@app.get("/users")
def get_users():
    users=["ali","abdullah"]
    return users

@app.post("/users")
def create_user(user:User):
    return user

@app.post("/vehical")
def create_vehical(model: str, company:str):
    return {"model":model, "Comapny":company}