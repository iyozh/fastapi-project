from pydantic import BaseModel


class PostBaseSchema(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePostSchema(PostBaseSchema):
    pass


class PostSchema(PostBaseSchema):
    id: int

    class Config:
        orm_mode = True
