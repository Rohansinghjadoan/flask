from fastapi import FastAPI
from pydantic import BaseModel
## pydantic validate input data and serialize output data
class User(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.get("/user",response_model=User)
def get_user():
    return User(id=1, name="rohan singh")
    