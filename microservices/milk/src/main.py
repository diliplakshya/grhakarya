from fastapi import FastAPI
import uvicorn
from .routers import milk


app = FastAPI()


app.include_router(milk.router)

@app.post("/")
async def create():
    return {"Samskriti": "Samskar"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)