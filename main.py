from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from utilities import getConvertedData
import json
from fastapi import Response

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
    return {"Hello": "World"}

@app.post("/convert")
def convert(imageBase64: str):
    print(getConvertedData(imageBase64))
    piotrek = getConvertedData(imageBase64)
    print(type(piotrek))
    # return Response(content=piotrek, media_type="application/json")
    return json.dumps(piotrek, indent=4)
    # return "ss"
