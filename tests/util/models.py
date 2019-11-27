from ..context import jsonty

# Python modules
from typing import List, Dict

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


class Toy(jsonty.Model):
    name: str
    uses: int

    def __init__(self, name: str, uses: int):
        self.name = name
        self.uses = uses


class Child(jsonty.Model):
    name: str
    age: int
    toys: list

    def __init__(self, name: str, age: int, toys: list):
        self.name = name
        self.age = age
        self.toys = toys


class ExampleList(jsonty.Model):
    ids: list

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

class ExampleTuple(jsonty.Model):
    values: tuple

    def __init__(self, values: tuple):
        self.values = values


class Adult(jsonty.Model):
        name: str
        age: int
        height: float
        working: bool

        def __init__(self, name: str, age: str, height: float, working: bool):
            self.name = name
            self.age = age
            self.height = height
            self.working = working

class NoModelClass():
    value: str

    def __init__(self, value: str):
        self.value = value

class ClassWithNoModel(jsonty.Model):
    number: int
    unknown_object: NoModelClass

    def __init__(self, number: str):
        self.number = number
        self.unknown_object = NoModelClass(value= 'Oops')    


class Car(jsonty.Model):
    name: str
    year: int
    
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year

class Driver(jsonty.Model):
    name: str
    car: Car
    
    def __init__(self, name: str, car: Car):
        self.name = name
        self.car = car

class Post(jsonty.Model):
    title: str
    tags: List[str]

    def __init__(self, title: str, tags: List[str]):
        self.title = title
        self.tags = tags

class Counter(jsonty.Model):
    data: Dict[str, int]
    
    def __init__(self, data: Dict[str, int]):
        self.data = data