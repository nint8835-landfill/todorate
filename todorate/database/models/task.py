from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from .base import Base, BaseDBModel

if TYPE_CHECKING:
    from .project import Project
    from .tag import Tag

tag_association = Table(
    "task_tag",
    Base.metadata,
    Column("task_id", ForeignKey("task.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)


class Task(BaseDBModel, Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("task.id"), nullable=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)

    children: list["Task"] = relationship("Task")
    parent: Optional["Task"] = relationship("Task", remote_side=[id])
    project: "Project" = relationship("Project")
    tags: list["Tag"] = relationship("Tag", secondary=tag_association)
