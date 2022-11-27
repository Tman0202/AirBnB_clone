#!/usr/bin/python3
"""Defines the basemodel class for other classes"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A class that is use as a Super class (base model) of all our classes.
        it defines all common attributes and methods for other classes to share """

    def __init__(self,*args, **kwargs):
        """used to construct the state of the object when first created"""
        if kwargs:
            for k in kwargs:
                if (k != '__class__'):
                    if (k == 'created_at' or k == 'updated_at'):
                        self.__setattr__(k, datetime.strptime(kwargs[k], '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        self.__setattr__(k, kwargs[k])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of the object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """update the updated_at attribute of this object when modified and saved"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """the dictionary representation of an object w/c is letter be used to serialize and deserialize the object"""
        new_dict = {}
        for k, v in self.__dict__.items():
            new_dict[k] = v
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)