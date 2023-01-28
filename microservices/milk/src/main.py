from fastapi import FastAPI
import uvicorn
from .routers import milk


app = FastAPI(debug=True)


app.include_router(milk.router)


@app.get("/")
async def home():
    return {"Samskriti": "Samskar"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5002, log_level="info", reload=True)