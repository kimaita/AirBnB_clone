#!/usr/bin/python3
"""This module defines the class Place"""

from models.base_model import BaseModel

class Place(BaseModel):
    """This class describes a residence"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if kwargs:
            Place.create_from_kwargs(self, kwargs)
        else:
            self.city_id = ''
            self.user_id = ''
            self.name = ''
            self.description = ''
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
