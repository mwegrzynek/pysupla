# -*- coding: UTF-8 -*-
from __future__ import print_function

import os.path
import sys
import warnings
import logging
from urllib.parse import urljoin


import requests


log = logging.getLogger(__name__)


class SuplaAPI:

    def __init__(self, server, personal_access_token):
        self.server = server
        self.base_url = 'https://{}/api/v2.3.0/'.format(server)
        self.session = requests.Session()
        self.session.headers['Authorization'] = 'Bearer {}'.format(personal_access_token)

    def get_server_info(self):
         with self.session.get(
            urljoin(self.base_url, 'server-info')
        ) as resp:
            return resp.json()

    def get_channels(self, include=None, func=None):
        params = {}

        if func is not None:
            params['function'] = ','.join(func)

        if include is not None:
            params['include'] = ','.join(include)

        with self.session.get(
            urljoin(self.base_url, 'channels'),
            params=params
        ) as resp:
            return resp.json()

    def get_channel(self, channel_id, include=None):
        params = {}

        if include is not None:
            params['include'] = ','.join(include)

        with self.session.get(
            urljoin(self.base_url, 'channels/{}'.format(channel_id)),
            params=params
        ) as resp:
            return resp.json()

    def execute_action(self, channel_id, action, **add_pars):
        params = dict(
            action=action
        )
        params.update(add_pars)

        with self.session.patch(
            urljoin(self.base_url, 'channels/{}'.format(channel_id)),
            json=params

        ) as resp:
            log.debug('Response for params %r: %r', params, resp.text)
            assert 200 < resp.status_code < 299