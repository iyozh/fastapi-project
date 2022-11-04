from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool

    class Config:
        orm_mode = True