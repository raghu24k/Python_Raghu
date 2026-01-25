from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional
class patient(BaseModel):
    name: str = Field(max_length= 50)
    email: EmailStr
    url: AnyUrl
    age: int = Field(gt=0,lt=100)
    weight: float = Field(gt = 0)
    married: bool
    allergies: Optional[list[str]] = None
    contact_details: dict[str, str]

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.url)
    print('inserted')

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('updated')
    # print(patient.allergies)

patient_info = {
    'name': 'raghuwinder',
    'email': 'abc@gmail.com',
    'url': 'https://www.google.com',
    'age': '32',
    'weight': '77',
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        # 'email': 'abc@gmail.com',
        'phone': '0987654321'
    }
}

patient1 = patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)
