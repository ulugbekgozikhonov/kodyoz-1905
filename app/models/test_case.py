import uuid
from app.db.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey

class TestCase(BaseModel):
    __tablename__ = "test_cases"

    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problems.id"), nullable=False)
    input_data: Mapped[str] = mapped_column(Text, nullable=False)
    expected_output: Mapped[str] = mapped_column(Text, nullable=False)
    
    problem = relationship("Problem", back_populates="test_cases")
