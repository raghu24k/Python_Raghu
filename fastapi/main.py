from fastapi import FastAPI, Path
import json

patient = FastAPI()

def LoadData():
    with open ('patients.json','r') as f:
        data = json.load(f)
    return data

@patient.get("/view")
def view():
    data = LoadData()
    return data

@patient.get('/patient/{patient_id}')
def ViewPatient(patient_id: str = Path(...,description="id of the patient in the db", example="p001")):
    # load all the patients
    data = LoadData()
    # Access the list of patients
    patients = data.get("patients", [])
    for p in patients:
        if p.get("patient_id") == patient_id:
            return p
    return {"message": "the patient is not found"}