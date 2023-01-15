from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from utilities import getConvertedData
import json
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Base64(BaseModel):
    imageBase64: str

@app.get("/")
def read_root():
    return {"204": "No Content"}

@app.post("/convert")
def convert(base64: Base64):
    return json.dumps(getConvertedData(base64.imageBase64))
