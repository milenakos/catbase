import json
from collections import UserDict

class CatDB(UserDict):
    def __init__(self, path, **kwargs):
        self.path = path
        
        try:
            self.autocommit = kwargs["autocommit"]
        except KeyError:
            self.autocommit = False
        
        try:
            self.safe = kwargs["safe"]
        except KeyError:
            self.safe = True
            
        try:
            self.none = kwargs["none"]
        except KeyError:
            self.none = None
        
        try:
            with open(path, 'r') as f:
                self.data = json.load(f)
        except IOError:
            self.data = {}
        except json.decoder.JSONDecodeError:
            if self.safe:
                raise
            print("Erorr decoding JSON, continuing from empty.")
            self.data = {}
            
    def commit(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f)

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.none
      
    # basically all of the below are just for autocommiting  
    def __setitem__(self, key, item):
        super().__setitem__(key, item)
        if self.autocommit:
            self.commit()

    def __delitem__(self, key):
        super().__delitem__(key)
        if self.autocommit:
            self.commit()

    def clear(self):
        result = super().clear()
        if self.autocommit:
            self.commit()
        return result

    def update(self, *args, **kwargs):
        result = super().update(*args, **kwargs)
        if self.autocommit:
            self.commit()
        return result

    def pop(self, *args):
        result = super().pop(*args)
        if self.autocommit:
            self.commit()
        return result

    def __cmp__(self, dict_):
        result = super().__cmp__(self, dict_)
        if self.autocommit:
            self.commit()
        return result