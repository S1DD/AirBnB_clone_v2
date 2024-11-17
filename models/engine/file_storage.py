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
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects
    
    def new(self, obj):
        """ Adds a new object to __objects with key <obj class name>.id """

        objcname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcname, obj.id)] = obj
    
    def save(self):
        """ Serializes __objects to the JSON file. """
        
        odict = FileStorage.__file_path
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
                json.dump(objdict, f)
    
    def reload(self):
        """Deserializes the JSON file to __objects, if the file exists."""
        
        try:
            with open(FileStorage.__file_path) as f:
                json_objs = json.load(f)
                for obj in json_objs.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**o))
        
        except FileNotFoundError:
            return
