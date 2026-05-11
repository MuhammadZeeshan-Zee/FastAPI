from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"welcome to home page"}
@app.get("/users")
def get_users():
    users=["ali","abdullah"]
    return users

@app.post("/users")
def post_user():
    return {"message":"user added"}