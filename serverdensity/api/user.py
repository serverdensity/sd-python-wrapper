from serverdensity import Response


class User(object):

    PATHS = {
        'create': '/users/users',
        'delete': '/users/users/{}',
        'list': '/users/users',
        'update': '/users/users/{}',
        'view': '/users/users/{}'
    }

    def __init__(self, api):
        self.api = api

    def create(self, data, **kwargs):
        return Response(self.api.post(url=self.PATHS['create'], data=data, **kwargs))

    def delete(self, _id, **kwargs):
        return Response(self.api.delete(url=self.PATHS['delete'].format(_id), **kwargs))

    def list(self, **kwargs):
        return Response(self.api.get(url=self.PATHS['list'], **kwargs))

    def update(self, _id, data, **kwargs):
        return Response(self.api.put(url=self.PATHS['update'].format(_id), data=data, **kwargs))

    def view(self, _id, **kwargs):
        return Response(self.api.get(url=self.PATHS['view'].format(_id), **kwargs))
