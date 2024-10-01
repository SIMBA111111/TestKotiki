import os

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncAttrs


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass