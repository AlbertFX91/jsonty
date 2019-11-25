# -*- coding: utf-8 -*-

# Python core imports
import unittest
import json

# Jsonty import
from ..context import jsonty

# Test models
import tests.util.models as models

class SimpleTypesLoads(unittest.TestCase):
    """Loads test operation with simple attributes via annotations"""

    def test_adult_dump(self):
        """ Test that a json representation of Aadult can be loads into its class """
        # Args
        name = 'Mathew'
        age = 24
        height = 1.82
        working = True
        # Dictionary construction
        data = {
            'name': name,
            'age': age,
            'height': height,
            'working': working
        }
        # Json representation
        json_str: str = json.dumps(data)
        # Object loads
        obj: models.Adult = models.Adult.loads(data=json_str)
        # Asserts
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.age, age)
        self.assertEqual(obj.height, height)
        self.assertEqual(obj.working, working)

if __name__ == '__main__':
    unittest.main()
