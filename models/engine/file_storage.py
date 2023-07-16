#!/usr/bin/python3
"""This module contains the definition of a FileStorage class"""
import json
import os

from models.base_model import BaseModel


class FileStorage:
    """..."""
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self) -> dict:
        """..."""
        return self.__objects

    def new(self, obj: object) -> None:
        """..."""
        key: str = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self) -> None:
        """..."""
        objs = {
            key: value.to_dict()
            for key, value in FileStorage.__objects.items()
        }
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(objs, file)

    def reload(self) -> None:
        """..."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                objs: dict = json.load(file)
                for value in objs.values():
                    cls_name = value["__class__"]
                    cls = eval(cls_name)
                    self.new(cls(**value))
