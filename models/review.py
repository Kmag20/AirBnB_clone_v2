#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    def __init__(self, *args, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
    # place_id = ""
    # user_id = ""
    # text = ""
