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

    def test_student_loads(self):
        """ Test that a json representation of Student can be loads into its class """
        # Args
        name = 'Mathew'
        age = 13
        grade = 14
        # Dictionary construction
        data = {
            'name': name,
            'age': age,
            'grade': 14,
        }
        # Json representation
        json_str: str = json.dumps(data)
        # Object loads
        obj: models.Student = models.Student.loads(data=json_str)
        # Asserts
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.age, age)
        self.assertEqual(obj.grade, grade)

if __name__ == '__main__':
    unittest.main()
