from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base, BaseDBModel

if TYPE_CHECKING:
    from .project import Project


class Tag(BaseDBModel, Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)

    project: "Project" = relationship("Project")
