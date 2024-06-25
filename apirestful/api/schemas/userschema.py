from typing import Union
from pydantic import BaseModel


# Schemas de User
class UserBaseSchema(BaseModel):
    username: str
    name: str
    email: str
    active: bool


class UserInSchema(BaseModel):
    username: str
    password: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
