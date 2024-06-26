from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Task(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(25),
        unique=True,
    )
