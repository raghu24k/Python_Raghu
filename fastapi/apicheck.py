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

@apicheck.get("/send")
def send():
    return{"message":"message not sending"}

@apicheck.get("/send/now")
def now():
    return{"message":"Your message is send successfully-->Raghuwinder kumar"}

@apicheck.get("/send/now/query")
def query():
    return{"Write":"your query is about file "}

@apicheck.get('/hello')
def hello():
    return{"Your message": "hi their is someone who lives here!!"}

@apicheck.get("/someone")
def someone():
    return{"message":"yes some here lived name rosahn"}

