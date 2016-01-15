from serverdensity import Response


class Service(object):

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

    def create(self, data, **kwargs):
        return Response(self.api.post(url=self.PATHS['create'], data=data, **kwargs))

    def delete(self, _id, **kwargs):
        return Response(self.api.delete(url=self.PATHS['delete'].format(_id), **kwargs))

    def list(self, **kwargs):
        result = self.api.get(url=self.PATHS['list'], **kwargs)
        return [Response(item) for item in result]

    def search(self, filtering, **kwargs):
        kwargs.setdefault('params', {})['filter'] = filtering
        result = self.api.get(url=self.PATHS['search'], **kwargs)
        return [Response(item) for item in result]

    def update(self, _id, data, **kwargs):
        return Response(self.api.put(url=self.PATHS['update'].format(_id), data=data, **kwargs))

    def view(self, _id, **kwargs):
        return Response(self.api.get(url=self.PATHS['view'].format(_id), **kwargs))
