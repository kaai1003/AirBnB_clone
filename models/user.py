#!/usr/bin/python3
"""Class user Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user definition"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
