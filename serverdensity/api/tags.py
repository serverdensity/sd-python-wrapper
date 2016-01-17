from serverdensity.api.crud import CRUD
from serverdensity.api.jsonobject import JsonObject


class Tags(JsonObject, CRUD):

    _schemapath = '/schema/tags.json'

    PATHS = {
        'create': '/inventory/tags',
        'delete': '/inventory/tags/{}',
        'list': '/inventory/tags',
        'update': '/inventory/tags/{}',
        'view': '/inventory/tags/{}'
    }
