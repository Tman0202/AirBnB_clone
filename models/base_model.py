import uuid
from datetime import datetime


class BaseModel:
    """A class that is use as a Super class (base model) of all our classes.
        it defines all common attributes and methods for other classes to share """

    def __init__(self):
        """used to construct the state of the object when first created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """update the updated_at attribute of this object when modified and saved"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """the dictionary representation of an object w/c is letter be used to serialize and deserialize the object"""
        new_dict = {}
        for k, v in self.__dict__.items():
            new_dict[k] = v
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
