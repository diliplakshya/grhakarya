from fastapi import FastAPI
import uvicorn
from enum import Enum
from pydantic import BaseModel
from typing import Union
from .db import client
from .dao import Dao


class Milk(BaseModel):
    quantity: int
    price: int
    description: Union[str, None] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

dao = Dao(client=client)


@app.get("/")
async def root():
    return {"message": "Samskriti Aur Samskar"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.post("/milk/")
async def create(milk: Milk):
    return Milk

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)