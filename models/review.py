#!/usr/bin/python3
"""
Module Review class
"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
