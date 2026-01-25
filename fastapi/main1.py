from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json
import os

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(description="ID of the patient", example="P001")]
    name: Annotated[str, Field(description="Name of the patient", example="Raghu")]
    city: Annotated[str, Field(description="City of the patient", example="Punjab")]
    age: Annotated[int, Field(gt=0, lt=120, description="Age of the patient", example=70)]
    gender: Annotated[Literal["male", "female", "others"], Field(description="Gender")]
    height: Annotated[float, Field(gt=0, description="Height in meters", example=1.75)]
    weight: Annotated[float, Field(gt=0, description="Weight in kg", example=55.0)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


def load_data():
    if not os.path.exists("patients.json"):
        return {}
    with open("patients.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    data[patient.id] = patient.model_dump(exclude=["id"])
    save_data(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient created successfully"}
    )
