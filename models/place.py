#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Table, Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))



class Place(BaseModel, Base):
    """ A place to stay """
    from models import storage_t
    if storage_t == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

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

    if storage_t != "db":
        @property
        def reviews(self):
            ''' Getter attrib returning the lost of review instances for file storage'''
            from models.review import Review
            from models.__init__ import storage
            review_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            from models.__init__ import storage
            amenity_list = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list