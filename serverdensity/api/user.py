from serverdensity.api.crud import CRUD


class User(CRUD):

    PATHS = {
        'create': '/users/users',
        'delete': '/users/users/{}',
        'list': '/users/users',
        'update': '/users/users/{}',
        'view': '/users/users/{}'
    }

    def __init__(self, api):
        self.api = api
