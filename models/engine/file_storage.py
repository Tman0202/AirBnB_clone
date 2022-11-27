#!/usr/bin/python3
"""Define the file storage class"""
import json
from os import path

class FileStorage:
    """An abstract storage engine
        Attributes:
            __file_path: path to the file to w/c the object to be serialized and deserialized
            __objects: a dictionary w/c is used to store objects of this class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects in the container(Dictionary)"""
        return FileStorage.__objects

    def new(self, obj):
        """sets __objects dictionary with key of <obj class name>.id and value obj"""
        name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """Serializes all objects from dictionary to json file"""
        new_dict = {}
        for k, v in FileStorage.__objects.items():
            new_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the json file to the __obects dictionary"""
        if path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path) as f:
                    objdict = json.load(f)
                    for o in objdict.values():
                        cls_name = o["__class__"]
                        del o["__class__"]
                        # after evaluating unpack dict(**)
                        self.new(eval(cls_name)(**o))
            except FileNotFoundError:
                return
