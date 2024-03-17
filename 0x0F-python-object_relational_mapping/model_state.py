#!/usr/bin/python3
""" object relatio mapping with sqlalchemy """
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """ define states object and map to states table in relational database """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
