from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
import models
import crud
from schemas import PostSchema, CreatePostSchema
from database import engine, SessionLocal, get_db

models.Base.metadata.create_all(bind=engine)

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
    post = crud.get_post_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.update_post(db=db, post=post, post_schema=post_schema)

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post_by_id(db=db, post_id=post_id)
    if not post.first():
        raise HTTPException(status_code=404, detail="Post not found")
    crud.delete_post(db=db, post=post)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
