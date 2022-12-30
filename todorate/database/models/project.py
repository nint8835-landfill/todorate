from sqlalchemy import Column, Integer

from .base import Base, BaseDBModel


class Project(BaseDBModel, Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
