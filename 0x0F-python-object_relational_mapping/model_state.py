#!/usr/bin/python3
"""
Contains a `State` class, a SQLAlchemy model that represents
a table called "states", with columns for id and name.
"""
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


if __name__ == "__main__":
    meta = MetaData()
    Base = declarative_base(metadata=meta)

    """Defines a SQLAlchemy model class called `State`
    """
    class State(Base):
        __tablename__ = "states"
        id = Column(Integer, unique=True, nullable=False, primary_key=True)
        name = Column(String(128), nullable=False)
