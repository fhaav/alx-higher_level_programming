#!/usr/bin/python3
""" Defines a City class for database representation """

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base

Base = declarative_base()


class City(Base):
    """ Represents a city in the database """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
