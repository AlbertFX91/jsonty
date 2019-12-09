# -*- coding: utf-8 -*-

# Python core imports
import unittest
import json

# Jsonty import
from ..context import jsonty

# Test models
import tests.util.models as models

class IterationDump(unittest.TestCase):
    """Dump test operation with simple attributes via annotations"""

    def test_toy(self):
        """ Test that the Toy class constructor works """
        # Args
        name = 'Car'
        uses = 5
        # Object construction
        obj = models.Toy(name=name, uses=uses)
        # Constructor class works
        self.assertIsNotNone(obj)
        # Check attributes
        self.assertEqual(name, obj.name)
        self.assertEqual(uses, obj.uses)

    def test_toy_dump(self):
        """ Test that the Toy class dumps works """
        # Args
        name = 'Car'
        uses = 5
        # Object construction
        obj = models.Toy(name=name, uses=uses)
        # Expected result
        expected = json.dumps({
            'name': name,
            'uses': uses
        })

        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)


    def test_child(self):
        """ Test that the Child class constructor works """
        # Args
        name = 'Mathew'
        age = 7
        toys = [models.Toy(name='Car', uses=5), models.Toy(name='Robot', uses=1)]
        # Object construction
        obj = models.Child(name=name, age=age, toys=toys)
        # Constructor class works
        self.assertIsNotNone(obj)
        # Check attributes
        self.assertEqual(name, obj.name)
        self.assertEqual(age, obj.age)
        self.assertEqual(toys, obj.toys)


    def test_list_model(self):
        """ Test that the Student with an iterable of a model class can be dumped """
        # Args
        name = 'Mathew'
        age = 15
        t1 = models.Toy(name='Car', uses=5)
        t2 = models.Toy(name='Robot', uses=1)
        toys = [t1, t2]
        # Object construction
        obj = models.Child(name=name, age=age, toys=toys)
        # Expected result
        expected = json.dumps({
            'name': name,
            'age': age,
            'toys': [
                {
                    'name': t1.name,
                    'uses': t1.uses
                },
                {
                    'name': t2.name,
                    'uses': t2.uses
                }
            ]
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)

    def test_set_model(self):
        """ Test that a Model with a set attribute can be dumped """
        # Args
        ids = [1, 2, 3, 4, 5, 6, 7, 8]
        # Object construction
        obj = models.ExampleList(ids=ids)
        # Expected result
        expected = json.dumps({
            'ids': ids
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)


    def test_dict_model(self):
        """ Test that a Model with a dictionary attribute can be dumped """
        # Args
        ids = {'arg0': 5, 'arg1': 2, 'arg2': [5, 9, 12]}
        # Object construction
        obj = models.ExampleDict(ids=ids)
        # Expected result
        expected = json.dumps({
            'ids': ids
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)

    def test_tuple_model(self):
        """ Test that a Model with a tuple attribute can be dumped """
        # Args
        values = (1, 2, 3, 'text', False)
        # Object construction
        obj = models.ExampleTuple(values=values)
        # Expected result
        expected = json.dumps({
            'values': values
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)

    def test_iter_with_model(self):
        """ Test that a Model with a dictionary attribute can be dumped """
        # Args
        int_model = models.ExampleInt(value=8)
        ids = [1, 4, 6, int_model]
        # Object construction
        obj = models.ExampleList(ids=ids)
        # Expected result
        expected = json.dumps({
            'ids': [1, 4, 6, {
                'value': int_model.value
            }]
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
