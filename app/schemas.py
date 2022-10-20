from datetime import datetime

from pydantic import BaseModel, EmailStr


class PostBaseSchema(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePostSchema(PostBaseSchema):
    pass


class PostSchema(PostBaseSchema):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserBaseSchema(BaseModel):
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool

    class Config:
        orm_mode = True