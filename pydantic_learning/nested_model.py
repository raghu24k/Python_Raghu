from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'mansa','state': 'punjab','pin': '151505'}
address1 = Address(**address_dict)
patient_dict = {'name':'raghu','gender': 'male','age':'22','address':address1}
patient1 = patient(**patient_dict)
print(patient1)