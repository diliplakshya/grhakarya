from fastapi import FastAPI, Depends
import uvicorn
from .security import User, get_current_active_user, oauth2_scheme
from .routers import login, milk


app = FastAPI(debug=True)


app.include_router(login.router)
app.include_router(milk.router)


@app.get("/", response_model=User)
async def home(current_user: User = Depends(get_current_active_user)):
    return {"Samskriti": "Samskar"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)