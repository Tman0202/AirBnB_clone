#!/usr/bin/python3
"""models folder is imported b/c we are using __init__ method"""
from datetime import datetime
from uuid import uuid4
import models



class BaseModel():
    """
    Parent class for AirBnB clone project
    Methods:
       
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: uuid4, dates when class was created/updated
        """
        
        if kwargs:
            for key,val in kwargs.items():
                if key !='__class__':
                    setattr(self, key, val)
                if  key == 'created_at' or key == 'updated_at':
                    time_format = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(val, time_format))  
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)        
        
        
    def __str__(self):
        """ str representation of classs"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """update attributes with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary containing all key value """  
        
        di = self.__dict__.copy()
        di['__class__']=self.__class__.__name__
        di['created_at']=datetime.isoformat(self.created_at)
        di['updated_at']=datetime.isoformat(self.updated_at)
        return di





