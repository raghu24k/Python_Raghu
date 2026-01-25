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

temp = patient1.model_dump() # model_dump() is for export make in 'dict' of your data collection
temp1 = patient1.model_dump_json() # and adding _json to make it 'str'
temp2 = patient1.model_dump(include=['name','gender'])
temp3 = patient1.model_dump(exclude=['name','gender'])
temp4 = patient1.model_dump(exclude={'address':['state']})


print(temp4)
print('hi type',type(temp))