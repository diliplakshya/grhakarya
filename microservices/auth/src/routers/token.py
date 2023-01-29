from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schemas.user_schema import UserCreate, User
from ..dependencies.oauth_dependency import oauth2_scheme
from ..service.token_service import authenticate_user, \
    generate_access_token, get_current_active_user, create_new_user
from ..dependencies.db_dependency import db_session
from ..schemas.token_schema import Token
from ..logging.logging import MyFileLogger


logger = MyFileLogger(__name__)


router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Token URL Not found"}},
)


@router.get("/")
async def token_home(token: str = Depends(oauth2_scheme)):
    return "Sharma"

@router.post("/create", response_model=User)
async def create(user: UserCreate, db: Session = Depends(db_session)):
    return create_new_user(db=db, user=user)

@router.get("/user", response_model=User)
async def get_user(user: UserCreate = Depends(get_current_active_user)):
    return user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_session)):
    logger.log_info("Logging User")
    user = authenticate_user(db=db, email=form_data.username, password=form_data.password)

    if not user:
        logger.log_error("Incorrect username or password")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = generate_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/user", response_model=User)
async def get_user(user: UserCreate = Depends(get_current_active_user)):
    return user
