from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional
class patient(BaseModel):
    name: str
    email: EmailStr
    # url: AnyUrl
    age: int 
    weight: float 
    married: bool
    allergies:list[str]
    contact_details: dict[str, str]

    @model_validator(mode= 'after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('patientss older than 60 must have an emergency contact')
        return model

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    # print(patient.url)
    print('inserted') 

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('updated')
    # print(patient.allergies)

patient_info = {
    'name': 'raghuwinder',
    'email': 'abc@icici.com',
    # 'url': 'https://www.google.com',
    'age': '88',
    'weight': '77',
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
    'emergency': '09876634',
        # 'email': 'abc@gmail.com',
        'phone': '0987654321'
    }
}

patient1 = patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)
