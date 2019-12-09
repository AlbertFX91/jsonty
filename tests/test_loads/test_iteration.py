# -*- coding: utf-8 -*-

# Python core imports
import unittest
import json

# Jsonty import
from ..context import jsonty

# Test models
import tests.util.models as models

class IterationDump(unittest.TestCase):
    """Loads test operation with iterate attributes via annotations"""

    def test_list_int_load(self):
        """ Test that a Model with a list of ints via typing can be loaded """
        # Args
        rates = [1, 2, 3, 5, 7]
        # Dictionary construction
        data = {
            'rates': rates
        }
        # Json representation
        json_str: str = json.dumps(data)
        # Object loads
        obj: models.Rate = models.Rate.loads(data=json_str)
        # Asserts
        self.assertEqual(obj.rates, rates)

    def test_list_model_load(self):
        """ Test that a Model with a list of models defined via typin can be loaded """
        # Args
        c1 = models.Car(name="Car 1", year="1991")
        c2 = models.Car(name="Car 2", year="1992")
        # Dictionary construction
        data = {            
            "cars": [
                {
                    'name': c1.name,
                    'year': c1.year
                },
                {
                    'name': c2.name,
                    'year': c2.year
                }
            ]
        }
        # Json representation
        json_str = json.dumps(data)
        # Object loads
        obj: models.CarCatalog = models.CarCatalog.loads(data=json_str)
        # Assertions
        self.assertEqual(obj.cars[0].name, c1.name)
        self.assertEqual(obj.cars[0].year, c1.year)
        self.assertEqual(obj.cars[1].name, c2.name)
        self.assertEqual(obj.cars[1].year, c2.year)
        
if __name__ == '__main__':
    unittest.main()
