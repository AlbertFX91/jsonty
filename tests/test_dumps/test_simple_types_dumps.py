# -*- coding: utf-8 -*-

from ..context import jsonty

import unittest

import json

class SimpleTypesDump(unittest.TestCase):
    """Dump test operation with simple attributes via annotations"""

    class Person(jsonty.Model):
        name: str
        age: int
        height: float
        working: bool

        def __init__(self, name: str, age: str, height: float, working: bool):
            self.name = name
            self.age = age
            self.height = height
            self.working = working
    

    def test_constructor(self):
        """ Check that the Person class constructor works """
        # Args
        name = 'Mathew'
        age = 24
        height = 1.82
        working = True

        # Object construction
        obj = self.Person(name=name, age=age, height=height, working=working)
        # Constructor class works
        self.assertIsNotNone(obj)

    def test_person_dump(self):
        """ Check that the Person class can be dumped into a json via annotations """
        # Args
        name = 'Mathew'
        age = 24
        height = 1.82
        working = True

        # Object construction
        obj = self.Person(name=name, age=age, height=height, working=working)
        
        # Expected result
        expected = json.dumps({
            'name': name,
            'age': age,
            'height': height,
            'working': working
        })
        
        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)



if __name__ == '__main__':
    unittest.main()
