from sqlalchemy.orm import Session
from app.models.users import User, UserCreate, UserUpdate


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username, email=user.email,
        password=user.password, full_name=user.full_name)
    db.add(db_user)
    try:
        db.commit()
    except:
        db.rollback()
        return None
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id)
    if db_user.first() is None:
        return False
    db_user.update(user.dict(exclude_unset=True))
    db.commit()
    return True


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
