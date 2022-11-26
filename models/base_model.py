import uuid
from datetime import datetime


class BaseModel:
    """A class that is use as a Super class (base model) of all our classes.
        it defines all common attributes and methods for other classes to share """

    def __init__(self,*args, **kwargs):
        """used to construct the state of the object when first created"""
        if kwargs:
            for k in kwargs:
                if (k != '__class__'):
                    if (k == 'created_at'):
                        self.__setattr__('created_at', datetime.strptime(kwargs[k], '%Y-%m-%dT%H:%M:%S.%f'))
                    if (k == 'updated_at'):
                        self.__setattr__('updated_at', datetime.strptime(kwargs[k], '%Y-%m-%dT%H:%M:%S.%f'))
                    if (k != 'created_at' and k != 'updated_at'):
                        self.__setattr__(k, kwargs[k])
        else:
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


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")

my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("--")
print(my_model is my_new_model)