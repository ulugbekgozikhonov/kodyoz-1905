from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

