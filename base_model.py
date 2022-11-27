#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
        Represents the BaseModel class for all
        objects in the AirBnb Clone Project
    """

    def __init__(self, *args, **kwargs):
        """Base model initialization"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    time_format = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, time_format))
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with the current datetime object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts all class attributes to a dictionary (json format)"""
        dicto = {
            '__class__': type(self).__name__,
            'created_at': datetime.isoformat(self.created_at),
            'updated_at': datetime.isoformat(self.updated_at)
        }
        dict_rep = dict(self.__dict__)
        dict_rep.update(dicto)
        return dict_rep

    def __str__(self):
        """ overriding the default str method to define the
            string representation of the BaseModel class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
