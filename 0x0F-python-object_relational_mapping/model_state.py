#!/usr/bin/python3
"""
Contains a `State` class, a SQLAlchemy model that represents
a table called "states", with columns for id and name.
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """Defines a SQLAlchemy model class called `State`
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
