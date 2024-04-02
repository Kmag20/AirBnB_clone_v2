#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for key, value in kwargs.items():
        #     if key != '__class__':
        #         setattr(self, key, value)
    # state_id = ""
    # name = ""
