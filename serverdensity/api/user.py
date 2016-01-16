from serverdensity.api.crud import CRUD
from serverdensity.api.jsonobject import JsonObject


class User(JsonObject, CRUD):

    _schemapath = '/schema/users.json'

    PATHS = {
        'create': '/users/users',
        'delete': '/users/users/{}',
        'list': '/users/users',
        'update': '/users/users/{}',
        'view': '/users/users/{}'
    }
