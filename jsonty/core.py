# -*- coding: utf-8 -*-

# Python modules
import json

# Python typing
from typing import List, Dict, Type

# Core classes


class Model():

    @staticmethod
    def get_dictionary_annotations(obj: any, cls_type: type):
        # Res dictionary
        res = dict()
        # Finding the bases class in order to get the parent Model annotations
        for base in cls_type.__bases__:
            if issubclass(base, Model):
                res.update(Model.get_dictionary_annotations(obj, base))
        # Recovering the annotations
        annotations: Dict[str, type] = cls_type.__dict__.get('__annotations__', {})
        # Field names
        f_names: List[str] = list(annotations.keys())
        # Field classes
        f_cls: List[type] = [annotations[f_name] for f_name in f_names]
        # Field processing
        for f_name, f_cls in zip(f_names, f_cls):
            print(f_name, f_cls)
            # If the field is a subclass of the model, recovering its annotations
            if issubclass(f_cls, Model):
                res[f_name] = Model.get_dictionary_annotations(obj, f_cls)
            else:
                res[f_name] = getattr(obj, f_name, None)
        return res

    class ModelEncode(json.JSONEncoder):
        def default(self, obj): # pylint: disable=E0202
            if issubclass(type(obj), Model):
                return Model.get_dictionary_annotations(obj, type(obj))
            else:
                return json.JSONEncoder.default(self, obj)

    @classmethod
    def get_annotations(cls: type):
        # Recovering the annotations
        annotations: Dict[str, type] = cls.__dict__.get('__annotations__', {})
        # Recovering the parent annotations of Model classes
        for base in cls.__bases__:
            if issubclass(base, Model):
                model_subclass: Type[Model]  = base
                annotations.update(model_subclass.get_annotations()) 
        return annotations
    
    def dumps(self, **kwargs):
        return json.dumps(self, cls=Model.ModelEncode, **kwargs)





        
