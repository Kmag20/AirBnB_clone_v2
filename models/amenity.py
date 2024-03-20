#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
    # name = ""
