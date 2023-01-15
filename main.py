from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from utilities import getConvertedData
import json
from fastapi import Response
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"204": "No Content"}

@app.post("/convert")
def convert(imageBase64: str):
    return json.dumps(getConvertedData(imageBase64))
