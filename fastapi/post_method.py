from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# @app.post('/create/name')
# def create_user():
#     return{'message':'You have successfully created user'}


users = []
class user(BaseModel):
    name: str
    age: int
@app.post('/user')
def create_user(user: user):
    users.append(user)
    return{
        # 'name': user.name,
        # 'age': user.age,
        'message': 'User Created ',
        'total user': len(users)
    }

@app.get('/user')
def get_users():
    return users



studentlist = []   # 👈 storage (RAM)

class AddStudent(BaseModel):   # 👈 Model
    student_name: str
    student_age: int
    student_class: int

@app.post("/addstudent")
def add_student(student: AddStudent):
    studentlist.append(student)   
    return {
        "student": student,
        "status": "student added",
        "total_students": len(studentlist)
    }
@app.get('/student')
def getstudents():
    return studentlist