"""
    Main module for API.

    This module is the main module for Fast API app.
"""

from fastapi import FastAPI
import uvicorn
from .db.connection import Base, engine
from .routers import token
from .config.config import settings
from .routers.sphinx import sphinx_routes


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
    title=settings.api_title,
    description=description,
    version=settings.api_version,
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
    routes=sphinx_routes(),
)

app.include_router(token.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return {"Samskriti": "Samskar"}

if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.api_host, port=settings.api_port, reload=True)
