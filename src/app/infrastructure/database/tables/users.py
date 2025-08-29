from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from app.infrastructure.database.tables.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
    )
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    language: Mapped[str]
