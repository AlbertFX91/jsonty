# -*- coding: utf-8 -*-

# Python modules
import json
from collections.abc import Iterable

# Python typing
from typing import List, Dict, Type

# Jsonty models
from .exceptions import TypeNotReconized
from .exceptions import IterableNotAllSameType

# Standard data types
_STANDARD_DATA_TYPES = {int, float, bool, str}

# ITERABLES EXCEPT DICT
_ITERABLE_NOT_DICT_DATA_TYPES = {list, set}

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

    def decode(self, data: dict, cls: Type[Model]) -> Type[Model]:
        # All annotations recovery
        annotations: Dict[str, type] = get_model_annotations(cls)

        # kwargs construction
        kwargs: Dict[str, object] = dict()
        
        # Kwargs population
        for f_name, f_cls in annotations.items():
            # If the field is an standard data type, use the stadard value
            if f_cls in _STANDARD_DATA_TYPES:
                kwargs[f_name] = self.on_standard_data_type(data, f_name)
            else:
                raise TypeNotReconized('{0}: {1} -> {2}'.format(cls, f_name, f_cls))

        # Object construction
        res: Type[Model] = cls(**kwargs)
        return res

    def on_standard_data_type(self, obj: dict, f_name: str):
        return obj.get(f_name, None)

class ModelEncode(json.JSONEncoder):

    def on_standard_data_type(self, obj, f_name, f_cls):
        return getattr(obj, f_name, None)

    def on_iterable_not_dict_data_type(self, obj, cls_type, f_name, f_cls):
        return list(getattr(obj, f_name, None))
        
    def on_dictionary_data_type(self, obj, cls_type, f_name, f_cls):
        return getattr(obj, f_name, None)

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
            # If the field is an standard data type, use the stadard value
            if f_cls in _STANDARD_DATA_TYPES:
                res[f_name] = self.on_standard_data_type(obj, f_name, f_cls)
            # If the class is an iterable but not a dict
            elif f_cls in _ITERABLE_NOT_DICT_DATA_TYPES:
                res[f_name] = self.on_iterable_not_dict_data_type(obj, cls_type, f_name, f_cls)
            # If the class is a dictionary
            elif f_cls is dict:
                res[f_name] = self.on_dictionary_data_type(obj, cls_type, f_name, f_cls)
            else:
                raise TypeNotReconized('{0}: {1} -> {2}'.format(cls_type, f_name, f_cls))

        return res

    def default(self, obj): # pylint: disable=E0202
        if issubclass(type(obj), Model):
            return self.get_dictionary_annotations(obj, type(obj))
        else:
            return json.JSONEncoder.default(self, obj)






        
