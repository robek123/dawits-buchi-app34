import logging
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_enginerom app.core.config import get_settings

logger = logging.getLogger()

echo = get_settings().database_echo

SQLALCHEMY_DATABASE_URL = f"{get_settings().database_url}/{{get_settings().database_name}}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=echo)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
