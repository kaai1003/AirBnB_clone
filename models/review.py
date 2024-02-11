#!/usr/bin/python3
"""Class review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review definition"""

    place_id = ""
    user_id = ""
    text = ""
