from fastapi import FastAPI
import uvicorn
from .db.connection import Base, engine
from .routers import token


description = """
Auth Microservide for grahakarya project. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="auth",
    description=description,
    version="0.1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Dilip Kumar Sharma",
        "url": "https://www.linkedin.com/in/diliplakshya/",
        "email": "diliplakshya@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    redoc_url=None,
)

app.include_router(token.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return {"Samskriti": "Samskar"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5001, log_level="info", reload=True)
