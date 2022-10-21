from datetime import timedelta, datetime
from typing import Union

from jose import jwt
from sqlalchemy import exists
from sqlalchemy.orm import Session, Query

from lib.constants import SECRET_KEY, ALGORITHM
from lib.models.post_model import Post
from lib.models.user_model import User
from lib.schemas.post_schema import CreatePostSchema
from lib.schemas.user_schema import UserCreateSchema
from lib.utils import verify_password, get_password_hash


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
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
