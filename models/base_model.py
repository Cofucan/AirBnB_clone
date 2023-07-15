#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """__init__ method for BaseModel class
        Args:
            args (tuple): arguments
            kwargs (dict): key word arguments
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation of BaseModel"""
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        """save method of BaseModel updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict method of BaseModel creates dict with all keys/values of
        __dict__ of the instance
        Returns:
            dictionary of instance key-value pairs
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
