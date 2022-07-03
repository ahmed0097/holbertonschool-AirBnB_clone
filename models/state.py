#!/usr/bin/python3
"""
Module State class
"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute:
    """
    name = ""
