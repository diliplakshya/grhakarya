from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas.user_schema import UserCreate, User
from ..dao.user_dao import get_user_by_email, create_user
from ..dependencies.oauth_dependency import oauth2_scheme
from ..service.token_service import authenticate_user, \
    generate_access_token, get_current_active_user


router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Token URL Not found"}},
)


@router.get("/")
async def token_home(token: str = Depends(oauth2_scheme)):
    return "Sharma"

@router.post("/create", response_model=User)
async def create(user: UserCreate):

    user = get_user_by_email(email=user.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate user.",
        )

    return create_user(user=user)

@router.get("/user", response_model=User)
async def get_user(user: UserCreate = Depends(get_current_active_user)):
    return user

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(email=form_data.username, password=form_data.password)

    if not user:
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
