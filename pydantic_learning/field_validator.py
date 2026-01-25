from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

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
