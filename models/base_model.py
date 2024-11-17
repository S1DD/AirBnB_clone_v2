#!/usr/bin/env python3

from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, id, *args, **kwargs):
        """ Initialize a new BaseModel instance """

        timefmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = created_at

        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        self.__dict__[k] = strptime(v, timefmt)
                    else:
                        self.__dict__[k] = v
            else:
                models.storage.new(self)

    def __str__(self):
        """ Return a string representation of the object. """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_cp = self.__dict__.copy()
        dict_cp[__class__] = __class__.__name__
        dict_cp["created_at"] = self.created_at.isoformat()
        dict_cp["updated_at"] = self.updated_at.isoformat()
        return dict_cp
