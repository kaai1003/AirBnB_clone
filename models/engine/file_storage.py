#!/usr/bin/python3
"""file storage module"""
import json
import os


class FileStorage:
    """file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionnary objects"""
        return self.__objects

    def new(self, obj):
        """add new object to objects dict
        Args:
            obj (dict): dict to object
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes objects dict to the JSON file"""
        json_dict = json.dumps(self.__objects)
        with open(self.__file_path, mode='w') as json_file:
            json_file.write(json_dict)

    def reload(self):
        """deserializes the JSON file to objects dict"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r') as json_file:
                json_dict = json_file.read()
            self.__objects = json.loads(json_dict)
