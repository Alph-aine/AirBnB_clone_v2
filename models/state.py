#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from os import getenv
from models.city import City
import shlex


class State(BaseModel, Base):
    """
    State class
    Attributes:
        name: input name

    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        city = relationship("City", cascade="all, delete,\
                            delete-orphan", backref="state")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            storage_access = models.storage.all()
            list_dict = []
            result = []
            for key in storage_access:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    list_dict.append(storage_access[key])
            for prop in list_dict:
                if (prop.state_id == self.id):
                    result.append(prop)
            return (result)
