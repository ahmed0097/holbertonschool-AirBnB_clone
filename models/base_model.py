#!/usr/bin/python3
""""this is the base model
"""
import uuid
from datetime import datetime

format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """this class will be the base of all other classes
    """


def __init__(self, *args, **kwargs):
    """" initialize  base model
    """
    """""generate unique id """
    if args is not None and len(args) > 0:
        pass
    if kwargs:
        for key, item in kwargs.item():
            if key in ['created_at', 'updated_at']:
                item = datetime.strptime(item, format_dt)
            if key not in ['__class__']:
                setattr(self, key, item)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        self.updated_at = datetime.now()


def __str__(self):
    """print: [<class name>] (<self.id>) <self.__dict__>
    """
    return "[{}] ({}) {}".format(
        self.__class__.__name__, self.id, self.__dict__)


def save(self):
    """Update updated_at with the current datetime."""
    self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all the keys/values of the instance."""
        
        dictionary = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dictionary[key] = item    
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
