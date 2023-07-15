#!/usr/bin/python3
"""FileStorage modeule"""
import json
from models import base_model


class FileStorage():
    """class FileStorage
    Attributes:
        __filepath (str): file path to JSON file
        __objects (dict): dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method returns dictionary of objects
        Returns:
        __objects - dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """new method which adds object to __objects dict
        Args:
            obj (object): object to add to dictionary
        """
        key = f"{self.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """save method serializes __object to JSON file at __filepath"""
        with open(self.__file_path, "w", encoding="utf-8") as file1:
            dic = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic, file1)

    def reload(self):
        "Reload method deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file1:
                obj_dict = json.load(file1)
                for obj_data in obj_dict.values():
                    cls_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(f"base_model.{cls_name}")(**obj_data))

        except FileNotFoundError:
            pass
