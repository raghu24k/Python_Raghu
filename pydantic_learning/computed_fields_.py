from pydantic import BaseModel, EmailStr, computed_field

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float      # in kg
    height: float      # in meters
    married: bool
    allergies: list[str]
    contact_details: dict[str, str]

    @computed_field
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


# ------------------ DATA ------------------

patient_info = {
    'name': 'raghuwinder',
    'email': 'abc@icici.com',
    'age': '32',
    'weight': '77',
    'height': '1.74',
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '0987654321'
    }
}

patient1 = Patient(**patient_info)

print("BMI:", patient1.bmi)
# print(patient1.model_dump())
