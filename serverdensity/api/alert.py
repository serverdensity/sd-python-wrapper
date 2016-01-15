from serverdensity import Response


class Alert(object):

    PATHS = {
        'create': '/alerts/configs',
        'delete': '/alerts/configs/{}',
        'list': '/alerts/configs',
        'list_by_subject': '/alerts/configs/{}',
        'update': '/alerts/configs/{}',
        'view': '/alerts/configs/{}',
        'triggered': '/alerts/triggered',
        'device_metrics': '/alerts/device_alerts.json',
        'service_metrics': '/alerts/service_alerts.json'
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

    def list_by_subject(self, subject_id, subject_type, **kwargs):
        kwargs.setdefault('params', {})['subjectType'] = subject_type
        result = self.api.get(
            url=self.PATHS['list_by_subject'].format(subject_id), **kwargs
        )
        return [Response(item) for item in result]

    def update(self, _id, data, **kwargs):
        return Response(self.api.put(url=self.PATHS['update'].format(_id), data=data, **kwargs))

    def view(self, _id, **kwargs):
        return Response(self.api.get(url=self.PATHS['view'].format(_id), **kwargs))

    def triggered(self, _id=None, subject_type=None, closed=None, **kwargs):
        if _id and subject_type:
            url = self.PATHS['triggered'] + '/{}'.format(_id)
            kwargs.setdefault('params', {})['subjectType'] = subject_type
        else:
            url = self.PATHS
        if closed:
            kwargs.setdefault('params', {})['closed'] = closed
        result = self.api.get(url=url, **kwargs)
        return [Response(item) for item in result]

    def device_metrics(self, **kwargs):
        return Response(self.api.get(url=self.PATHS['device_metrics'], **kwargs))

    def service_metrics(self, **kwargs):
        return Response(self.api.get(url=self.PATHS['service_metrics'], **kwargs))
