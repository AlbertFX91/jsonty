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

    
    def test_model_inside_model(self):  
        """ Test that when a class has a non model object, an excetion is raised """
        # Args
        car_name = 'BMW'
        year = 2010
        driver_name = 'James'
        # Dictionary construction
        data = {
            'name': driver_name,
            'car': {
                'name': car_name,
                'year': year
            }
        }
        # Json representation
        json_str: str = json.dumps(data)
        # Object loads
        obj: models.Driver = models.Driver.loads(data=json_str)
        # Asserts
        self.assertEqual(obj.name, driver_name)
        self.assertEqual(obj.car.name, car_name)
        self.assertEqual(obj.car.year, year)
    
    def test_type_not_reconized_exception(self):  
        """ Test that when a class has a non model object, an exception is raised """
        # Dictionary construction
        data = {
            'number': 1,
            'unknown_object': {
                'value': "oops"
            }
        }
        # Json representation
        json_str: str = json.dumps(data)

        self.assertRaises(jsonty.exceptions.TypeNotReconized, models.ClassWithNoModel.loads, json_str)

if __name__ == '__main__':
    unittest.main()
