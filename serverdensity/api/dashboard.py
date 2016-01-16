from serverdensity.api.crud import CRUD


class Dashboard(CRUD):

    PATHS = {
        'create': '/users/dashboards',
        'delete': '/users/dashboards/{}',
        'list': '/users/dashboards',
        'update': '/users/dashboards/{}',
        'view': '/users/dashboards/{}'
    }

    def __init__(self, api):
        self.api = api
