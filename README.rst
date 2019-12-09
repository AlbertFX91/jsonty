******
Jsonty
******
Jsonty is an automatic JSON serialization/deseralization Python library for your custom classes.

.. image:: https://travis-ci.com/AlbertFX91/jsonty.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.com/AlbertFX91/jsonty

.. image:: https://img.shields.io/github/issues-raw/AlbertFX91/jsonty
    :alt: GitHub issues
    :target: https://github.com/AlbertFX91/jsonty/issues

.. image:: https://coveralls.io/repos/github/AlbertFX91/jsonty/badge.svg?branch=master
    :alt: Coverage
    :target: https://coveralls.io/github/AlbertFX91/jsonty?branch=master

.. image:: https://img.shields.io/github/license/AlbertFX91/jsonty
    :alt: License
    :target: LICENSE


How it works
################
Jsonty serialize and deserialize your custom objects by its annotations. All you have to do is define its attributes and make sure that are added in the constructor

.. code-block:: python

   import jsonty
   class Toy(jsonty.Model):
       name: str
       uses: int

       def __init__(self, name: str, uses: int):
           self.name = name
           self.uses = uses
   # Object creation
   toy: Toy = Toy(name='white car', uses=10)
   # Dumps operation
   toy_json: str = toy.dumps() # { 'name': 'white car', 'uses': 10 }
   # Loads operation
   toy_recoverying: Toy = Toy.loads(toy_json) # The json representation is converted into a Toy object

Operations supported
####################
There are a range of types that jsonty can handle such as:

 * Basic data types: *str, int, bool, number*
 * Iterables: *List, Dict, Set, Tuple*
 * Model Inheritance

Links
####################
* pypi: https://pypi.org/project/jsonty/
* github: https://github.com/AlbertFX91/jsonty

