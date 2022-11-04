from datetime import timedelta
from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import crud
from api.api_v1.routers import api_router
from lib.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from lib.schemas.post_schema import PostSchema, CreatePostSchema
from lib.schemas.token_schema import Token



# @app.post("/posts/", response_model=PostSchema)
# def create_post(post: CreatePostSchema, db: Session = Depends(get_db)):
#     return crud.create_post(db=db, post=post)
#
#
# @app.get("/posts/", response_model=List[PostSchema])
# def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     posts = crud.get_posts(db, skip=skip, limit=limit)
#     return posts
#
# @app.get("/posts/{post_id}", response_model=PostSchema)
# def get_post(post_id: int, db: Session = Depends(get_db)):
#     post = crud.get_post_by_id(db=db, post_id=post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return post
#
# @app.put("/posts/{post_id}", response_model=PostSchema)
# def update_post(post_id: int, post_schema: CreatePostSchema, db: Session = Depends(get_db)):
#     if not crud.check_post_if_exists(db=db, post_id=post_id):
#         raise HTTPException(status_code=404, detail="Post not found")
#
#     post = crud.get_post_by_id(db=db, post_id=post_id, is_query=True)
#     return crud.update_post(db=db, post=post, post_schema=post_schema)
#
# @app.delete("/posts/{post_id}")
# def delete_post(post_id: int, db: Session = Depends(get_db)):
#     post = crud.get_post_by_id(db=db, post_id=post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#
#     crud.delete_post(db=db, post=post)
#
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
#
# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = crud.authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = crud.create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

app = FastAPI()
app.include_router(api_router, prefix="/api_v1")
if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)

