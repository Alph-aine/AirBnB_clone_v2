#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """
    State class
    Attributes:
        name: input name

    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        city = relationship("City",  backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            all_cities = models.storage.all(City)
            city_list = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
