from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/return")
def home():
    return("hey:""i am comeback")