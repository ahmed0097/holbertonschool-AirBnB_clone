#!/usr/bin/python3
"""Test_BaseModel module"""


from models.base_model import BaseModel
from models import *
import unittest
from datetime import datetime
import uuid


class Test_BaseModel(unittest.TestCase):
    """testing BaseModel"""

    def test_base_model_uuid_good_format(self):
        """
        Tests if UUID is in the correct format.
        """
        bm = BaseModel()
        self.assertIsInstance(uuid.UUID(bm.id), uuid.UUID)

    def test_attributes(self):
        """Check for attributes."""
        base1 = BaseModel()
        self.assertEqual(str, type(base1.id))
        self.assertEqual(datetime, type(base1.created_at))
        self.assertEqual(datetime, type(base1.updated_at))

        base2 = BaseModel(id=4, created_at='2017-06-14T22:31:03.285259')
        self.assertEqual(base2.id, 4)
        self.assertEqual(datetime, type(base2.created_at))

    def test_str(self):
        """test the str output"""
        b3 = BaseModel()
        string = f"[{b3.__class__.__name__}] ({b3.id}) {b3.__dict__}"
        self.assertEqual(str(b3), string)

    def test_todict(self):
        """test if the object is converted to dict"""
        b5 = BaseModel()
        mydict = b5.to_dict()
        self.assertEqual(mydict['__class__'], 'BaseModel')
        self.assertEqual(type(mydict['created_at']), str)
        self.assertEqual(type(mydict['updated_at']), str)


if __name__ == "__main__":
    unittest.main()
