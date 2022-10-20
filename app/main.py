from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session, declarative_base
import models
import crud
from app.schemas.post_schema import PostSchema, CreatePostSchema
from app.schemas.user_schema import UserSchema, UserCreateSchema
from database import engine, SessionLocal, get_db

Base = declarative_base()
Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.post("/posts/", response_model=PostSchema)
def create_post(post: CreatePostSchema, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)


@app.get("/posts/", response_model=List[PostSchema])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=PostSchema)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=PostSchema)
def update_post(post_id: int, post_schema: CreatePostSchema, db: Session = Depends(get_db)):
    if not crud.check_post_if_exists(db=db, post_id=post_id):
        raise HTTPException(status_code=404, detail="Post not found")

    post = crud.get_post_by_id(db=db, post_id=post_id, is_query=True)
    return crud.update_post(db=db, post=post, post_schema=post_schema)

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    crud.delete_post(db=db, post=post)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
