#!/usr/bin/python3
"""class BaseModel Module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel Class
    """

    def __init__(self, *args, **kwargs):
        """instance attribute method constructor
        + create instance from dictionnary
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return str of instance"""
        class_name = str(self.__class__.__name__)
        class_dict = str(self.__dict__)
        return "[" + class_name + "] (" + self.id + ") " + class_dict

    def save(self):
        """update instance attribute update_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """method return dict with all
        key/values of __dict__ instance"""
        inst_dict = {}
        inst_dict['__class__'] = self.__class__.__name__
        for key in self.__dict__:
            if key == "created_at":
                inst_dict[key] = datetime.isoformat(self.__dict__[key])
            elif key == "updated_at":
                inst_dict[key] = datetime.isoformat(self.__dict__[key])
            else:
                inst_dict[key] = self.__dict__[key]
        return inst_dict
