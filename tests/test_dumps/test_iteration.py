# -*- coding: utf-8 -*-

from ..context import jsonty

import unittest

import json

class InterationDump(unittest.TestCase):
    """Dump test operation with simple attributes via annotations"""

    class Subject(jsonty.Model):
        name: str
        grade: int

        def __init__(self, name: str, grade: int):
            self.name = name
            self.grade = grade

    class Student(jsonty.Model):
        name: str
        age: int
        subjects: list

        def __init__(self, name: str, age: int, subjects: list):
            self.name = name
            self.age = age
            self.subjects = subjects

    class ExampleSet(jsonty.Model):
        ids: set

        def __init__(self, ids):
            self.ids = ids

        def __hash__(self):
            return hash(tuple(self.ids))

    
    class ExampleDict(jsonty.Model):
        ids: dict

        def __init__(self, ids):
            self.ids = ids

    class ExampleInt(jsonty.Model):
        value: int

        def __init__(self, value):
            self.value = value

    def test_subject(self):
        """ Check that the Subject class constructor works """
        # Args
        name = 'Maths'
        grade = 1
        # Object construction
        obj = self.Subject(name=name, grade=grade)
        # Constructor class works
        self.assertIsNotNone(obj)
        # Check attributes
        self.assertEqual(name, obj.name)
        self.assertEqual(grade, obj.grade)

    def test_subject_dump(self):
        """ Check that the Subject class dumps works """
        # Args
        name = 'Maths'
        grade = 1
        # Object construction
        obj = self.Subject(name=name, grade=grade)
        # Expected result
        expected = json.dumps({
            'name': name,
            'grade': grade
        })

        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)


    def test_student(self):
        """ Check that the Student class constructor works """
        # Args
        name = 'Mathew'
        age = 15
        subjects = [self.Subject(name='Maths', grade=1), self.Subject(name='English', grade=1)]
        # Object construction
        obj = self.Student(name=name, age=age, subjects=subjects)
        # Constructor class works
        self.assertIsNotNone(obj)
        # Check attributes
        self.assertEqual(name, obj.name)
        self.assertEqual(age, obj.age)
        self.assertEqual(subjects, obj.subjects)


    def test_list_model(self):
        """ Check that the Student with an iterable of a model class can be dumped """
        # Args
        name = 'Mathew'
        age = 15
        s1 = self.Subject(name='Maths', grade=1)
        s2 = self.Subject(name='English', grade=1)
        subjects = [s1, s2]
        # Object construction
        obj = self.Student(name=name, age=age, subjects=subjects)
        # Expected result
        expected = json.dumps({
            'name': name,
            'age': age,
            'subjects': [
                {
                    'name': s1.name,
                    'grade': s1.grade
                },
                {
                    'name': s2.name,
                    'grade': s2.grade
                }
            ]
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)

    def test_set_model(self):
        """ Check that a Model with a set attribute can be dumped """
        # Args
        ids = [1, 2, 3, 4, 5, 6, 7, 8]
        # Object construction
        obj = self.ExampleSet(ids=ids)
        # Expected result
        expected = json.dumps({
            'ids': ids
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)


    def test_dict_model(self):
        """ Check that a Model with a dictionary attribute can be dumped """
        # Args
        ids = {'arg0': 5, 'arg1': 2, 'arg2': [5, 9, 12]}
        # Object construction
        obj = self.ExampleDict(ids=ids)
        # Expected result
        expected = json.dumps({
            'ids': ids
        })
        
        # Dumps operation
        res = obj.dumps()
        
        self.assertEqual(res, expected)

    def test_iter_with_model(self):
        """ Check that a Model with a dictionary attribute can be dumped """
        # Args
        int_model = self.ExampleInt(value=8)
        ids = {1, 4, 6, int_model}
        # Object construction
        obj = self.ExampleSet(ids=ids)
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
