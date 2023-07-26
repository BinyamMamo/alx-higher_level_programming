#!/usr/bin/python3
"""
Contains a `State` class, a SQLAlchemy model that represents
a table called "states", with columns for id and name.
"""
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlAlchemy.ext.declarative import declarative_base


meta = MetaData()
Base = declarative_base(metadata=meta)
if __name__ == "__main__":
    class State(Base):
        """
        Defines a SQLAlchemy model class called `State`
        """
        __tablename__ = "states"
        id = Column(Integer, unique=True, nullable=False, primary_key=True)
        name = Column(String(128), nullable=False)
