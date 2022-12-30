from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from .base import Base, BaseDBModel

if TYPE_CHECKING:
    from .project import Project


class User(BaseDBModel, Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    projects: list["Project"] = relationship("Project", uselist=True)
