#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from mock import patch
from serverdensity.api import ApiClient
from serverdensity.api import User


class UserTest(unittest.TestCase):

    @patch.object(ApiClient, '_make_request')
    def setUp(self, mock_make_request):
        self.client = ApiClient('aeou')
        self.client._make_request = mock_make_request
        self.client._make_request.return_value = {'user': 'result'}
        self.user = User(api=self.client)

    def test_user_create(self):
        data = {'data': 'user'}
        self.user.create(data)
        self.client._make_request.assert_called_with(
            data=data,
            method='POST',
            url=User.PATHS['create'],
            params=None
        )

    def test_user_delete(self):
        self.user.delete(1)
        self.client._make_request.assert_called_with(
            data=None,
            method='DELETE',
            url=User.PATHS['delete'].format(1),
            params=None
        )

    def test_user_list(self):
        self.client._make_request.return_value = [{'user': 'result'}]
        self.user.list()
        self.client._make_request.assert_called_with(
            data=None,
            method='GET',
            url=User.PATHS['list'],
            params=None
        )

    def test_user_update(self):
        data = {'name': 'test', 'type': 'user'}
        self.user.update(_id=1, data=data)
        self.client._make_request.assert_called_with(
            data=data,
            method='PUT',
            url=User.PATHS['update'].format(1),
            params=None
        )

    def test_user_view(self):
        self.user.view(1)
        self.client._make_request.assert_called_with(
            data=None,
            method='GET',
            url=User.PATHS['view'].format(1),
            params=None
        )

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
