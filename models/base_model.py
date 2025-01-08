#!/usr/bin/env python3

from datetime import datetime
import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime, Column, String

Base = declarative_base()


class BaseModel:
    """Defines the BaseModel class.
    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        

        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = str(type(self).__name__)
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict.pop("_sa_instance_state", None)
        return rdict

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        clname = self.__dict__.copy()
        clname.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, clname)
