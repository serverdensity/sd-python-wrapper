from serverdensity import Response


class Metrics(object):

    PATHS = {
        'available': '/metrics/definitions/{}',
        'get': '/metrics/graphs/{}'
    }

    def __init__(self, api):
        self.api = api

    def available(self, _id, start, end, **kwargs):
        kwargs.setdefault('params', {})['start'] = start.isoformat()
        kwargs['params']['end'] = end.isoformat()
        result = self.api.get(url=self.PATHS['available'].format(_id), **kwargs)
        return [Response(item) for item in result]

    def get(self, _id, start, end, filtering, **kwargs):
        kwargs.setdefault('params', {})['start'] = start.isoformat()
        kwargs['params']['end'] = end.isoformat()
        kwargs['params']['filter'] = filtering
        result = self.api.get(url=self.PATHS['get'].format(_id), **kwargs)
        return [Response(item for item in result)]
