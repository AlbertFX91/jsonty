# -*- coding: utf-8 -*-

from ..context import jsonty

import unittest

import json

class InheritanceDump(unittest.TestCase):
    """Dump test operation with simple attributes with inheritance"""

    class Person(jsonty.Model):
        name: str
        age: int

        def __init__(self, name: str, age: str):
            self.name = name
            self.age = age
    
    class Student(Person):
        grade: int
        
        def __init__(self, name: str, age: str, grade: int):
            super().__init__(name=name, age=age)
            self.grade = grade
    

    def test_constructor(self):
        """ Check Student class constructor works """
        # Args
        name = 'Mathew'
        age = 13
        grade = 14

        # Object construction
        obj = self.Student(name=name, age=age, grade=grade)
        # Constructor class works
        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.grade, grade)

    def test_student_dump(self):
        """ Check Student class can be dumped into a json via annotations """
        # Args
        name = 'Mathew'
        age = 13
        grade = 14

        # Object construction
        obj = self.Student(name=name, age=age, grade=grade)
        
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
