#!/usr/bin/python3
""" This module implements the User class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ User class implementation """
    def __init__(self, *args, **kwargs):
        """ Setting up initialization for User class
            *args: Is not been used
        """
        class_attr = ["city_id", "user_id", "description", "name",
                      "number_rooms", "number_bathrooms", "max_guest",
                      "price_by_night", "latitude", "longitude",
                      "amenity_ids"]
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        if kwargs:
            sub_dict = {k: kwargs[k] for k in class_attr if kwargs.get(k)}
            nargs = {k: v for (k, v) in kwargs.items() if k not in class_attr}
            super().__init__(**nargs)
            self.__dict__.update(sub_dict)
        else:
            super().__init__()
