from fastapi import FastAPI, Path , HTTPException, Query
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
    raise HTTPException(status_code = 404, detail="patient not found")


@patient.get('/sort')
def sort_patient(sort_by:str=Query(...,description="sort on the basis of age, height"), order:str = Query('asc',description="sort in asc or desc order")):
    vaild_field = ['age','height']
    if sort_by not in vaild_field:
        raise HTTPException(Status_code=404,detail="Invaild field select from {Vaild_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invaild order select between asc and desc')

    data = LoadData()
    sort_order = True if order =='desc' else False
    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order)
    return sorted_data