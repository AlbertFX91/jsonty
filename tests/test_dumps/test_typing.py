# -*- coding: utf-8 -*-

# Python core imports
import unittest
import json

# Jsonty import
from ..context import jsonty

# Test models
import tests.util.models as models

class TypingDump(unittest.TestCase):
    """Dump test operation with attributes anottated as typing"""

    def test_post_list(self):
        """ Test that the Post class which a List type can be dumped"""
        # Args
        title = 'title'
        tags = ['tag1', 'tag2', 'tag3']
        # Object construction
        obj = models.Post(title=title, tags=tags)
         # Expected result
        expected = json.dumps({
            'title': title,
            'tags': tags
        })

        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)

    def test_counter_dict(self):
        """ Test that the Counter class which a Dict type can be dumped"""
        # Args
        data = {
            'words': 15,
            'lines': 2
        }
        # Object construction
        obj = models.Counter(data=data)
         # Expected result
        expected = json.dumps({
            "data": data
        })

        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)


    def test_rates_list(self):
        """ Test that the Counter class which a Dict type can be dumped"""
        # Args
        rates = [1, 2, 3, 5, 7]
        # Object construction
        obj = models.Rate(rates=rates)
         # Expected result
        expected = json.dumps({
            "rates": rates
        })

        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)

    def test_list_of_models(self):
        """ Test that the Counter class which a Dict type can be dumped"""
        # Args
        c1 = models.Car(name="Car 1", year="1991")
        c2 = models.Car(name="Car 2", year="1992")
        cars = [c1, c2]
        # Object construction
        obj = models.CarCatalog(cars=cars)
         # Expected result
        expected = json.dumps({
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
        })

        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
