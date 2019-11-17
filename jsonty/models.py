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
    def dumps(self, **kwargs):
        return json.dumps(self, cls=ModelEncode, **kwargs)

class ModelEncode(json.JSONEncoder):


    def on_model_subclass(self, obj, f_name, f_cls):
        return self.get_dictionary_annotations(obj, f_cls)

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
            # If the field is a subclass of the model, recovering its annotations
            if issubclass(f_cls, Model):
                res[f_name] = self.on_model_subclass(obj, f_name, f_cls)
            # If the field is an standard data type, use the stadard value
            elif f_cls in _STANDARD_DATA_TYPES:
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






        
