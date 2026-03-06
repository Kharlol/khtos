from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Author(Base):
    """Автор фото - пользователь Telegram."""

    __tablename__ = 'authors'


class Photo(Base):
    """Фотография, присланная в бот Telegram."""

    __tablename__ = 'photos'
