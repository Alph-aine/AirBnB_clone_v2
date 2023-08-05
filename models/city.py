#!/usr/bin/python3
""" City Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from models.place import Place
from os import getenv


class City(BaseModel, Base):
    """ The city class
    Attributes:
        state_id: id of the state
        name: input nanme
    """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        '''initializes city'''
        super().__init__(*args, **kwargs)
