from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
rom app.core.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    disabled = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=current_timestamp())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())

    @property
    def is_active(self):
        return not self.disabled


def __repr__(self):
    return f'<User> {self.id}, {self.username}, {self.email}'


class UserCreate(Base):
    username: str
    email: str
    password: str
    full_name: str = None


class UserUpdate(UserCreate):
    password: str = None
