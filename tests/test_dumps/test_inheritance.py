# -*- coding: utf-8 -*-

# Python core imports
import unittest
import json

# Jsonty import
from ..context import jsonty

# Test models
import tests.util.models as models

class InheritanceDump(unittest.TestCase):
    """Dump test operation with simple attributes with inheritance"""

    def test_constructor(self):
        """ Test that Student class constructor works """
        # Args
        name = 'Mathew'
        age = 13
        grade = 14

        # Object construction
        obj = models.Student(name=name, age=age, grade=grade)
        # Constructor class works
        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.grade, grade)

    def test_student_dump(self):
        """ Test that Student class can be dumped into a json via annotations """
        # Args
        name = 'Mathew'
        age = 13
        grade = 14

        # Object construction
        obj = models.Student(name=name, age=age, grade=grade)
        
        # Expected result
        expected = json.dumps({
            'name': name,
            'age': age,
            'grade': grade
        })
        
        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)



if __name__ == '__main__':
    unittest.main()
