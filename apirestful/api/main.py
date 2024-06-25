from datetime import timedelta

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from api import categoriesrouter, podcastsrouter, authorsrouter
from api import tags_metadata
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from api import get_db, securitycontroller
from api import UserCreateSchema, UserSchema, UserInSchema

from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

# Origins permitidos politica CORS
origins = [
    "http://127.0.0.1:5500"
]

# Apirestful con FastApi
app = FastAPI(
    title="Mastermind Podcast API",
    description="ApiRestFul para la gestión de los podcast realizados por Mastermind",
    version="0.1",
    contact={
        "name": "Paco Gómez",
        "url": "http://www.mastermind.ac"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importacion de las rutas
app.include_router(
    categoriesrouter,
    tags=["categories"],
    prefix="/categories")

app.include_router(
    podcastsrouter,
    tags=["podcasts"],
    prefix="/podcasts")

app.include_router(
    authorsrouter,
    tags=["authors"],
    prefix="/authors")

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@app.post("/signup/", response_model=UserSchema)
async def signup(user: UserCreateSchema, db: Session = Depends(get_db)):
    user.password=pwd_context.hash(user.password)
    return securitycontroller.write_user(db,user)

@app.post("/signin/")
async def login(user: UserInSchema, db: Session = Depends(get_db)):
    user = securitycontroller.authenticate_user(db, user.username, user.password, pwd_context)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {"access_token": securitycontroller.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    ), "token_type": "bearer"}
