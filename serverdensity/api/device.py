from serverdensity import Response


class Device(object):

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

    def create(self, data, **kwargs):
        return Response(self.api.post(url=self.PATHS['create'], data=data, **kwargs))

    def delete(self, _id, **kwargs):
        return Response(self.api.delete(url=self.PATHS['delete'].format(_id), **kwargs))

    def list(self, **kwargs):
        return Response(self.api.get(url=self.PATHS['list'], **kwargs))

    def search(self, filtering, **kwargs):
        kwargs.setdefault('params', {})['filter'] = filtering
        return Response(self.api.get(url=self.PATHS['search'], **kwargs))

    def update(self, _id, data, **kwargs):
        return Response(self.api.put(url=self.PATHS['update'].format(_id), data=data, **kwargs))

    def view_by_agent(self, agentkey, **kwargs):
        return Response(self.api.get(url=self.PATHS['view_by_agent'].format(agentkey), **kwargs))

    def view(self, _id, **kwargs):
        return Response(self.api.get(url=self.PATHS['view'].format(_id), **kwargs))
