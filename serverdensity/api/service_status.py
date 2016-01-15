from serverdensity import Response


class ServiceStatus(object):

    PATHS = {
        'overall': '/service-monitor/meta/{}',
        'location': '/service-monitor/last/{}'
    }

    def __init__(self, api):
        self.api = api

    def overall(self, _id, **kwargs):
        return Response(self.api.get(url=self.PATHS['overall'].format(_id), **kwargs))

    def location(self, _id, **kwargs):
        result = self.api.get(url=self.PATHS['location'].format(_id), **kwargs)
        return [Response(item) for item in result]
