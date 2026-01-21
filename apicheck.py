from fastapi import FastAPI

apicheck = FastAPI()

@apicheck.get("/")
def home():
    return {"message": "hello apichecker"}

# undo = FastAPI()
@apicheck.get("/undo")
def undo():
    return{"message": "Undo Changed"}

@apicheck.get('/undo/repo')
def repo():
    return{"message": "Your repo is in process"}