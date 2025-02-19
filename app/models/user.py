from app.db.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, Date
from datetime import date

import enum

class GenderType(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class User(BaseModel):
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(String(length=33), unique=True,nullable=False)
    firstname: Mapped[str] = mapped_column(String(length=50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(length=50))
    photo_url: Mapped[str] = mapped_column(String(length=255))
    email: Mapped[str] = mapped_column(String(length=125), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    gender: Mapped[GenderType] = mapped_column(Enum(GenderType,name="gender_enum"))
    birth_date: Mapped[date] = mapped_column(Date)
    