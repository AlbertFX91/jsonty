# -*- coding: utf-8 -*-

from .context import jsonty

import unittest

import json

class SimpleTypesDump(unittest.TestCase):
    """Advanced test cases."""

    class SimpleSingleTypes(jsonty.Model):
        string: str
        n_int: int
        n_float: float
        boolean: bool

        def __init__(self, string: str, n_int: int, n_float: float, boolean: bool):
            self.string = string
            self.n_int = n_int
            self.n_float = n_float
            self.boolean = boolean

    def test_constructor(self):
        # Args
        string = 'Example string'
        n_int = 15243
        n_float = 4.93
        boolean = True

        # Object construction
        obj = self.SimpleSingleTypes(string=string, n_int=n_int, n_float=n_float, boolean=boolean)
        # Constructor class works
        self.assertIsNotNone(obj)

    def test_static_dump(self):
        # Args
        string = 'Example string'
        n_int = 15243
        n_float = 4.93
        boolean = True

        # Object construction
        obj = self.SimpleSingleTypes(string=string, n_int=n_int, n_float=n_float, boolean=boolean)
        
        # Expected result
        expected = json.dumps({
            'string': string,
            'n_int': n_int,
            'n_float': n_float,
            'boolean': boolean
        })
        
        # Dumps operation
        res = obj.dumps()

        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
