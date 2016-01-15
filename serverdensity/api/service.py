from serverdensity import Response
from serverdensity.api.crud import CRUD


class Service(CRUD):

    PATHS = {
        'create': '/inventory/services',
        'delete': '/inventory/services/{}',
        'list': '/inventory/services',
        'search': '/inventory/resources',
        'update': '/inventory/services/{}',
        'view': '/inventory/services/{}'
    }

    def __init__(self, api):
        self.api = api

    def search(self, filtering, **kwargs):
        kwargs.setdefault('params', {})['filter'] = filtering
        result = self.api.get(url=self.PATHS['search'], **kwargs)
        return [Response(item) for item in result]
