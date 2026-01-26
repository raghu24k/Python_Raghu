from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, field_validator

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
    student_course: str
    student_fees: int

    @field_validator("student_fees")
    @classmethod
    def convert_fees(cls,value):
        if value <= 0:
            raise ValueError("fees must be greater than 0")
        return f"{value} Rs"

@app.post("/addstudent")
def add_student(student: AddStudent):
    student_data ={
        'id': len(studentlist)+1,
        'student name': student.student_name,
        'student age': student.student_age,
        'student class': student.student_class,
        'student course': student.student_course,
        'student fees': student.student_fees
    }
    studentlist.append(student_data)   
    return {
        'id': len(studentlist)+1,
        "student": student,
        "status": "student added",
        "total_students": len(studentlist)
    }
@app.get('/student')
def getstudents():
    return studentlist