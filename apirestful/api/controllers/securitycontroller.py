from datetime import timedelta, datetime, timezone
from typing import Annotated, Union

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from starlette import status

from api import UserModel, UserCreateSchema, get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin/")

SECRET_KEY = "a2c052d7bcda5ffedeb9725be9aae6a98b4876136963475d8941df4c9660162f"
ALGORITHM = "HS256"


def get_user(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


# Registramos usuario
def write_user(db: Session, user: UserCreateSchema):
    user = UserModel(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, username: str, password: str, pwd_context):
    user = get_user(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user


def check_token(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    # Comprobación de usuario en DB
    # No es un sistema de token seguro, solo de implementacion de oAuth2
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = get_user(db, username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except NoResultFound:
        user = None
    return user







def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
