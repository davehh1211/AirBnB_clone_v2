#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if STORAGE == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""
