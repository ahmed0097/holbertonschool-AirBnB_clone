#!/usr/bin/python3
"""
Module Amenity class
"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute:
    """
    name = ""
