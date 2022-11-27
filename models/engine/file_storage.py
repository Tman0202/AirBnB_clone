#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        This class serializes instances to a JSON file
        and deserializes JSON file to instances, It thus
        represents an abstracted storage engine.
        Attributes:
        __file_path (str): The path to the name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = 'airbnb_file.json'
    __objects = {}

    def all(self):
        """Returns all the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id."""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        dicobject = {}
        for key in self.__objects.keys():
            dicobject[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf8') as json_file:
            json.dump(dicobject, json_file)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf8') as json_file:
                dicobjecto = json.load(json_file)
                for obj in dicobjecto.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
