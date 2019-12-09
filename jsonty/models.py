# -*- coding: utf-8 -*-

# Python modules
import json
import sys
from collections.abc import Iterable

# Python typing
from typing import List, Dict, Type, _GenericAlias, TypeVar

# Jsonty models
from .exceptions import TypeNotReconized
from .exceptions import IterableNotAllSameType

# Standard data types
_STANDARD_DATA_TYPES = {int, float, bool, str}

# ITERABLES EXCEPT DICT
_ITERABLE_NOT_DICT_DATA_TYPES = {list, set, tuple}


class Model():
    def dumps(self, **kwargs) -> str:
        """ Convert the Model object into a json string """
        return json.dumps(self, cls=ModelEncode, **kwargs)

    @classmethod
    def loads(cls, data: str):
        """ Convert string json representation of a model into a Model object """
        data_dict = data
        if type(data) == str:
            data_dict = json.loads(data_dict)
        # Object decode
        res = ModelDecode().decode(data_dict, cls)
        return res


def get_model_annotations(cls: Type[Model]) -> Dict[str, type]:
    res: Dict[str, type] = dict()

    # Recovering all the annotations of all the parent Model classes
    for base in cls.__bases__:
        if issubclass(base, Model):
            res.update(get_model_annotations(base))
    
    # Recovering the current Model class annotations
    annotations: Dict[str, type] = cls.__dict__.get('__annotations__', {})

    # Updating the dictionary resulted
    res.update(annotations)

    return res

class ModelDecode():

    def on_typing(self, data: dict, f_name: str, f_cls: type, cls: Type[Model]):
        """ Recover the attribute f_name from obj which is typed as f_cls"""
        res = None
        # Getting the origin class from the type
        type_class = f_cls.__origin__
        # Value of the field
        object_value = data.get(f_name)
        if type_class in (list, set, tuple):
            # value type recovering
            type_value = f_cls.__args__[0]
            # Type arg not defined, so using the value
            if(type(type_value) == TypeVar):
                res = type_class(object_value)
            # If the type of the elements is a dict, call the constructior using kwargs unpacking 
            if type(object_value[0]) is dict:
                res = type_class([type_value(**val) for val in object_value])
            # If the arg type has been defined, using its constructor
            else:
                res = type_class([type_value(val) for val in object_value])


        return res

    def on_type(self, data: dict, f_name: str, f_cls: type, cls: Type[Model]):
        """ Recover the attribute f_name from obj which is typed as f_cls"""
        res = None
         # If the field is an standard data type, use the stadard value
        if f_cls in _STANDARD_DATA_TYPES:
            res = self.on_standard_data_type(data, f_name)
        # If the attribute is a Model subclass
        elif issubclass(f_cls, Model):
            res = self.on_model_subclass_type(data, f_name, f_cls)
        else:
            raise TypeNotReconized('{0}: {1} -> {2}'.format(cls, f_name, f_cls))
        return res

    def decode(self, data: dict, cls: Type[Model]) -> Type[Model]:
        
        # All annotations recovery
        annotations: Dict[str, type] = get_model_annotations(cls)

        # kwargs construction
        kwargs: Dict[str, object] = dict()
        
        # Kwargs population
        for f_name, f_cls in annotations.items():
            # If the attribute is from typing
            if type(f_cls) == _GenericAlias:
                kwargs[f_name] = self.on_typing(data, f_name, f_cls, cls)
            else:
                kwargs[f_name] = self.on_type(data, f_name, f_cls, cls)

        # Object construction
        res: Type[Model] = cls(**kwargs)
        return res

    def on_standard_data_type(self, obj: dict, f_name: str):
        return obj.get(f_name, None)

    def on_model_subclass_type(self, obj: dict, f_name: str, f_cls: Type[Model]):
        # Subclass model object construction
        res = self.decode(obj.get(f_name), f_cls)
        return res


class ModelEncode(json.JSONEncoder):

    def on_standard_data_type(self, obj, f_name, f_cls):
        return getattr(obj, f_name, None)

    def on_iterable_not_dict_data_type(self, obj, f_name, f_cls):
        return list(getattr(obj, f_name, None))
        
    def on_dictionary_data_type(self, obj, f_name, f_cls):
        return getattr(obj, f_name, None)

                
    def on_model_subclass_type(self, obj, f_name, f_cls):
        return self.default(getattr(obj, f_name))

    def on_typing(self, obj, f_name, f_cls):
        """ Recover the attribute f_name from obj which is typed as f_cls"""
        res = None
        # Getting the origin class from the type
        type_class = f_cls.__origin__
        if type_class in _ITERABLE_NOT_DICT_DATA_TYPES:
            res = self.on_iterable_not_dict_data_type(obj, f_name, f_cls)
        elif type_class is dict:
            res = self.on_dictionary_data_type(obj, f_name, f_cls)
        else:
            raise TypeNotReconized('{0}: {1} -> {2}'.format(type(obj), f_name, f_cls))
        return res

    def on_type(self, obj, f_name, f_cls):
        """ Recover the attibute f_name from obj which is from the class f_cls """ 
        res = None
        # If the field is an standard data type, use the stadard value
        if f_cls in _STANDARD_DATA_TYPES:
            res = self.on_standard_data_type(obj, f_name, f_cls)
        # If the class is an iterable but not a dict
        elif f_cls in _ITERABLE_NOT_DICT_DATA_TYPES:
            res = self.on_iterable_not_dict_data_type(obj, f_name, f_cls)
        # If the class is a dictionary
        elif f_cls is dict:
            res = self.on_dictionary_data_type(obj, f_name, f_cls)
        # If the attribute is a Model subclass
        elif issubclass(f_cls, Model):
            res = self.on_model_subclass_type(obj, f_name, f_cls)
        else:
            raise TypeNotReconized('{0}: {1} -> {2}'.format(type(obj), f_name, f_cls))
        return res

    def get_dictionary_annotations(self, obj: any, cls_type: type):
        # Res dictionary
        res = dict()
        # Finding the bases class in order to get the parent Model annotations
        for base in cls_type.__bases__:
            if issubclass(base, Model):
                res.update(self.get_dictionary_annotations(obj, base))
        # Recovering the annotations
        annotations: Dict[str, type] = cls_type.__dict__.get('__annotations__', {})
        # Field names
        f_names: List[str] = list(annotations.keys())
        # Field classes
        f_cls: List[type] = [annotations[f_name] for f_name in f_names]
        # Field processing
        for f_name, f_cls in zip(f_names, f_cls):
            # If the attribute is from typing
            if type(f_cls) == _GenericAlias:
                res[f_name] = self.on_typing(obj, f_name, f_cls)
            else:
                res[f_name] = self.on_type(obj, f_name, f_cls)
            

        return res

    def default(self, obj): # pylint: disable=E0202
        if issubclass(type(obj), Model):
            return self.get_dictionary_annotations(obj, type(obj))






        
