import json

from serverdensity.wrapper.jsonobject import JsonObject
from serverdensity import Response


class Metrics(JsonObject):

    PATHS = {
        'available': '/metrics/v3/metrics/',
        'get': '/metrics/v3/query/'
    }

    def _validation(self, value):
        """Not needed"""
        pass

    def available(self, **kwargs):
        kwargs.setdefault('params', {})['page'] = "1"
        result = self.api.get(url=self.PATHS['available'], **kwargs)
        return result

    def get(self, start, end, requests, **kwargs):
        kwargs.setdefault('params', {})['start'] = start
        kwargs['params']['end'] = end
        kwargs['params']['requests'] = json.dumps(requests)
        result = self.api.get(url=self.PATHS['get'], **kwargs)
        return [Response(item) for item in result['series']]
