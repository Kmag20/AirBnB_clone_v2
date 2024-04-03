#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    from models import storage_t
    if storage_t == "db":
        __tablename__ = "places"
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # amenity_ids = []
