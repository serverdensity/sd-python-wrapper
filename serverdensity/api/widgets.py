from serverdensity import Response
from serverdensity.api.crud import CRUD


class Widget(CRUD):

    PATHS = {
        'create': '/users/widgets',
        'delete': '/users/widgets/{}',
        'list': '/users/widgets',
        'update': '/users/widgets/{}',
        'view': '/users/widgets/{}',
        'duplicate': '/users/widgets/duplicate/{}'
    }

    def __init__(self, api):
        self.api = api

    def duplicate(self, _id, **kwargs):
        return Response(self.api.post(url=self.PATHS['duplicate'].format(_id)))
