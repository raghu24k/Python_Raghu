from fastapi import FastAPI, Path, HTTPException,Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import json
app = FastAPI()

class patient(BaseModel):
    id: Annotated[str,Field(...,description='id of the patient',example='[P001]')]
    name: Annotated[str,Field(...,description='Name of the patient',examples='Ankit' 'Raghu')]
    city: Annotated[str,Field(...,description='City of the patient',examples='Punjab')]
    age: Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient',examples='70')]
    gender: Annotated[Literal['male','female','others'],Field(...,description='gender required')]
    height: Annotated[float,Field(...,gt=0,description='height of the patient')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the patient',examples='55kg')]

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)


