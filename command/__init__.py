# __init__.py
import os as _os
import pkgutil as _pkgutil
import importlib as _importlib

for (_, _name, _) in _pkgutil.iter_modules([_os.path.dirname(__file__)]):
    _importlib.import_module('.' + _name, __package__) #import __package__.name
