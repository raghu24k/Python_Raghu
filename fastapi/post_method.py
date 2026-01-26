from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.post('/create/name')
def create_user():
    return{'message':'You have successfully created user'}

class user(BaseModel):
    name: str
    age: int
@app.post('/user')
def create_user(user: user):
    return{
        'name': user.name,
        'age': user.age,
        'message': 'User Created '
    }