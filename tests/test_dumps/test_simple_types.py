# -*- coding: utf-8 -*-

# Python core imports
import unittest
import json

# Jsonty import
from ..context import jsonty

# Test models
import tests.util.models as models

class SimpleTypesDump(unittest.TestCase):
    """Dump test operation with simple attributes via annotations"""

    def test_constructor(self):
        """ Test that the Adult class constructor works """
        # Args
        name = 'Mathew'
        age = 24
        height = 1.82
        working = True

        # Object construction
        obj = models.Adult(name=name, age=age, height=height, working=working)
        # Constructor class works
        self.assertIsNotNone(obj)

    def test_person_dump(self):
        """ Test that the Adult class can be dumped into a json via annotations """
        # Args
        name = 'Mathew'
        age = 24
        height = 1.82
        working = True

        # Object construction
        obj = models.Adult(name=name, age=age, height=height, working=working)
        
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

    def test_type_not_reconized_exception(self):  
        """ Test that when a class has a non model object, an excetion is raised """

        oops = models.ClassWithNoModel(number=1)

        self.assertRaises(jsonty.exceptions.TypeNotReconized, oops.dumps)

    def test_model_inside_model(self):  
        """ Test that when a class has a non model object, an exception is raised """
        # Args
        car_name = 'BMW'
        year = 2010
        driver_name = 'James'
        car = models.Car(name=car_name, year=year)

        # Object construction
        obj = models.Driver(name=driver_name, car=car)

        # Expected result
        expected = json.dumps({
            'name': driver_name,
            'car': {
                'name': car_name,
                'year': year
            },
        })

        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
