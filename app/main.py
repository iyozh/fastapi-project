from typing import Union, Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/posts')
def get_posts():
    return {"data": ["This is your posts"]}

@app.post('/create_post')
def create_post(post: Post):
    print(post)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)