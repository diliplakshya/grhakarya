from fastapi import Depends, HTTPException, status, APIRouter
from ..security import Token, authenticate_user, fake_users_db
from ..utils.password_helper import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from ..config import settings
from sqlalchemy.orm import Session
from .. import dao, models, schemas
from ..db import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Token URL Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/user", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = dao.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="Email Already registered")

    return dao.create_user(db, user)

@router.post("/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to login. Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
