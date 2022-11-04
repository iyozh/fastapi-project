from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db
from lib import repos
from lib.schemas.user_schema import UserSchema, UserCreateSchema

router = APIRouter()

@router.post("/", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = repos.user.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repos.user.create(db=db, obj_in=user)


@router.get("/", response_model=list[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = repos.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = repos.user.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
