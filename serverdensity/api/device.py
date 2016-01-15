from serverdensity import Response
from serverdensity.api.crud import CRUD


class Device(CRUD):

    PATHS = {
        'create': '/inventory/devices',
        'delete': '/inventory/devices/{}',
        'list': '/inventory/devices',
        'search': '/inventory/resources',
        'update': '/inventory/devices/{}',
        'view_by_agent': '/inventory/devices/{}/byagentkey',
        'view': '/inventory/devices/{}'
    }

    def __init__(self, api):
        self.api = api

    def search(self, filtering, **kwargs):
        kwargs.setdefault('params', {})['filter'] = filtering
        result = self.api.get(url=self.PATHS['search'], **kwargs)
        return [Response(item) for item in result]

    def view_by_agent(self, agentkey, **kwargs):
        return Response(self.api.get(url=self.PATHS['view_by_agent'].format(agentkey), **kwargs))
