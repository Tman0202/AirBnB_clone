#!/usr/bin/python3
"""define the file storage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances, It thus
    represents an abstracted storage engine.
    Attributes:
    __file_path (str): The path to the name of the file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method wich returns dictionary __objects"""
        0
        return FileStorage.__objects
        # we can also use self.__object

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        # self.__object['{}.{}'.format(obj.__class__.__name__,obj.id]

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        dict_obj = {}
        for key, value in FileStorage.__objects.items():
            dict_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as j:
            json.dump(dict_obj, j)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""

        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as j:
                reloded = json.load(j)
                for key in reloded.keys():
                    new_obj = eval(reloded[key]["__class__"])(**reloded[key])
                    self.new(new_obj)
        except FileNotFoundError:
            return
