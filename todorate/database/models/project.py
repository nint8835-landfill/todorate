from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base, BaseDBModel

if TYPE_CHECKING:
    from .tag import Tag
    from .task import Task
    from .user import User


class Project(BaseDBModel, Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("project.id"), nullable=True)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    children: list["Project"] = relationship("Project")
    parent: Optional["Project"] = relationship("Project", remote_side=[id])
    tasks: list["Task"] = relationship("Task")
    owner: "User" = relationship("User")
    tags: list["Tag"] = relationship("Tag")
