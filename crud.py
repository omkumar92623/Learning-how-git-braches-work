from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

users= []

class Create_user(BaseModel):
    name:str
    classs:int
    roll_no:int

@app.post("/create_user")
def create_user(user:Create_user):
    users.append(user)
    return{
        "Msg":"User created",
        "data":user
    }


@app.get("/get_details")
def get_students():
    return users