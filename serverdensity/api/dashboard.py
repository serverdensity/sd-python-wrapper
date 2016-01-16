from serverdensity.api.crud import CRUD
from serverdensity.api.jsonobject import JsonObject


class Dashboard(JsonObject, CRUD):

    _schemapath = '/schema/dashboards.json'

    PATHS = {
        'create': '/users/dashboards',
        'delete': '/users/dashboards/{}',
        'list': '/users/dashboards',
        'update': '/users/dashboards/{}',
        'view': '/users/dashboards/{}'
    }
