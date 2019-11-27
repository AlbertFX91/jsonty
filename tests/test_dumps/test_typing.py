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

if __name__ == '__main__':
    unittest.main()
