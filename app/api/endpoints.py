from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.services import user_servicerom app.api.models import UserInfo, UserUpdate
from app.models.users import UserCreate


def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users


def get_user_info(user: User = Depends(get_current_user)) -> UserInfo:
    return UserInfo(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        disabled=user.disabled,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


def update_user(update_user: UserUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = user_service.update_user(db, user.id, update_user)
    if user:
        return {'message': 'User updated successfully.'}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Could not update user',
            headers={'WWW-Authenticate': 'Bearer'},)


router = APIRouter()


@router.get('/users/', response_model=List[UserInfo])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get('/users/me/', response_model=UserInfo)
def read_user_me(current_user: User = Depends(get_current_user)):
    return get_user_info(current_user)


@router.post('/users/', response_model=UserInfo, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.create_user(db, user=user)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username or email already registered',
            headers={'WWW-Authenticate': 'Bearer'},)
    elif db_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Could not create user',
            headers={'WWW-Authenticate': 'Bearer'},)
    return get_user_info(db_user)


@router.put('/users/me/', status_code=status.HTTP_200_OK)
def update_user_info(user: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    update_user(user, current_user, db)
