from database import Base

from sqlalchemy import Integer, String, Column, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    created_at: Mapped[str] = mapped_column(default=func.now())
    updated_at: Mapped[str] = mapped_column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now(),
    )


class BreedsModel(BaseModel):
    __tablename__ = 'breeds'

    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    cats: Mapped[list["CatsModel"]] = relationship("CatsModel", back_populates="breed", cascade="all, delete-orphan")


class CatsModel(BaseModel):
    __tablename__ = 'cats'

    color: Mapped[str] = mapped_column(String, index=True)
    age: Mapped[int] = mapped_column(Integer, index=True)
    description: Mapped[str] = mapped_column(String, index=True)
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"))

    breed: Mapped["BreedsModel"] = relationship(back_populates="cats")
