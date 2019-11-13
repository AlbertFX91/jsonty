# -*- coding: utf-8 -*-

# Python modules
import json

# Python typing
from typing import List, Dict, Type

# Jsonty models
from .exceptions import TypeNotReconized

# Standard data types
_STANDARD_DATA_TYPES = {int, float, bool, str}

class Model():
    def dumps(self, **kwargs):
        return json.dumps(self, cls=ModelEncode, **kwargs)

class ModelEncode(json.JSONEncoder):


    @staticmethod
    def get_dictionary_annotations(obj: any, cls_type: type):
        # Res dictionary
        res = dict()
        # Finding the bases class in order to get the parent Model annotations
        for base in cls_type.__bases__:
            if issubclass(base, Model):
                res.update(ModelEncode.get_dictionary_annotations(obj, base))
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
                res[f_name] = ModelEncode.get_dictionary_annotations(obj, f_cls)
            elif f_cls in _STANDARD_DATA_TYPES:
                res[f_name] = getattr(obj, f_name, None)
            else:
                raise TypeNotReconized('{0}: {1} -> {2}'.format(cls_type, f_name, f_cls))

        return res

    def default(self, obj): # pylint: disable=E0202
        if issubclass(type(obj), Model):
            return ModelEncode.get_dictionary_annotations(obj, type(obj))
        else:
            return json.JSONEncoder.default(self, obj)






        
