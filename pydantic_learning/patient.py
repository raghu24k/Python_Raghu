from pydantic import BaseModel

class patient(BaseModel):
    name: str
    age: int

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'raghu', 'age': '22'}
patient1 = patient(**patient_info)
insert_patient(patient1)