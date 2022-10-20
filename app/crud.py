from sqlalchemy.orm import Session, Query
from models import Post
from schemas import CreatePostSchema


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: CreatePostSchema):
    db_item = Post(**post.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def delete_post(db: Session, post: Post):
    db.delete(post)
    db.commit()

def update_post(db: Session, post: Query, post_schema: CreatePostSchema):
    post.update(post_schema.dict())
    db.commit()

    return post.first()
