from collections.abc import Mapping
import os.path
import json

from jsonschema import Draft4Validator
from jsonschema import FormatChecker
from jsonschema.compat import str_types
from jsonschema.exceptions import ValidationError
from bson.objectid import ObjectId


@FormatChecker.cls_checks(format='mongoId', raises=())
def is_mongoid(instance):
    if not isinstance(instance, str_types):
        return True
    return ObjectId.is_valid(instance)

FORMATCHECKER = FormatChecker()


class JsonObject(Mapping):

    _protected = [
        'values',
        'items',
        'keys',
        'get'
    ]

    _set_internally = [
        'api',
        '_data',
        '_validator',
        '_schemaobj'
    ]

    _schemapath = ''
    _schemaobj = {}
    _validator = None

    def __init__(self, api=None, *arrgs, **kwargs):
        self._data = {}
        if isinstance(api, dict):
            kwargs.update(api)
        else:
            self.api = api
        if kwargs:
            self._data.update(kwargs)
            self._validation(kwargs)
        if arrgs:
            for arg in arrgs:
                if isinstance(arg, dict):
                    self._data.update(arg)
            self._validation(self._data)

    def _set_schemaobj(self, path):
        path = os.path.dirname(__file__) + self._schemapath
        with open(path, 'r') as f:
            self._schemaobj = json.load(f)

    def _validation(self, data):
        if not self._schemaobj:
            self._set_schemaobj(self._schemapath)
        if not self._validator:
            self._validator = Draft4Validator(
                schema=self._schemaobj,
                format_checker=FORMATCHECKER
            )
        try:
            self._validator.validate(self._data)
        except ValidationError as e:
            raise AttributeError(e.message)

    def __iter__(self):
        return (key for key in self._data.keys())

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if key in self._protected:
            raise AttributeError('This is a protected property')
        if self._data:
            self._validation(dict(self._data))
            self._data[key] = value

    def __getattr__(self, name):
        attr = self._data.get(name)
        if attr:
            return attr
        else:
            raise AttributeError('Attribute does not exist')

    def __setattr__(self, name, value):
        if name in self._protected:
            raise AttributeError('This is a protected property')

        if name in self._set_internally:
            object.__setattr__(self, name, value)
        else:
            self._data[name] = value
            self._validation(self._data)
