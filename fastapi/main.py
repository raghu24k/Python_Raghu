from fastapi import FastAPI
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