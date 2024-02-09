#!/usr/bin/python3
"""class BaseModel Module"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class
    """

    def __init__(self):
        """instance attribute method constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return str of instance"""
        class_name = str(self.__class__.__name__)
        class_dict = str(self.__dict__)
        return "[" + class_name + "] (" + self.id + ") " + class_dict

    def save(self):
        """update instance attribute update_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """method return dict with all 
        key/values of __dict__ instance"""
        inst_dict = dict()
        for key in self.__dict__:
            return inst_dict
    