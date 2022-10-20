from sqlalchemy import exists
from sqlalchemy.orm import Session, Query

from app.models.post_model import Post
from app.models.user_model import User
from app.schemas.post_schema import CreatePostSchema
from app.schemas.user_schema import UserCreateSchema


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: CreatePostSchema):
    db_item = Post(**post.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_post_by_id(db: Session, post_id: int, is_query: bool = False):
    post = db.query(Post).filter(Post.id == post_id)
    return post if is_query else post.first()

def delete_post(db: Session, post: Post):
    db.delete(post)
    db.commit()

def update_post(db: Session, post: Query, post_schema: CreatePostSchema):
    post.update(post_schema.dict())
    db.commit()

    return post.first()

def check_post_if_exists(db: Session, post_id: int):
    return db.query(exists().where(Post.id == post_id)).scalar()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreateSchema):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
