#!/usr/bin/env python3

from datetime import datetime
import uuid
import models


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    """Base class for all our classes"""

    def __init__(self, *args, **kwargs):
        """ deserialize and serialize a class """
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs['id']

        if 'created_at' not in kwargs:
            self.created_at = datetime.today()
        else:
            self.created_at = datetime.strptime(kwargs['created_at'], tform)

        if 'updated_at' not in kwargs:
            self.updated_at = datetime.today()
        else:
            self.updated_at = datetime.strptime(kwargs['updated_at'], tform)

        if kwargs:
            for k, v in kwargs.items():
                if k not in ['created_at', 'updated_at', 'id']:
                    self.__dict__[k] = v
        else:

            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
