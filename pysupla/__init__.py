# -*- coding: UTF-8 -*-
from __future__ import print_function

import os.path
import sys
import warnings
from urllib.parse import urljoin


import requests


class SuplaAPI:

    def __init__(self, server, personal_access_token):
        self.base_url = f'https://{server}/api/v2.3.0/' 
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'Bearer {personal_access_token}'

    def get_channels(self, include=None, func=None):
        params = {}

        if func is not None:
            params = {'function': ','.join(func)}

        with self.session.get(
            urljoin(self.base_url, 'channels'),
            params=params
        ) as resp:
            return resp.json()

    def execute_action(self, channel_id, action, **add_pars):
        params = dict(
            action=action
        )
        params.update(add_pars)

        with self.session.patch(
            urljoin(self.base_url, f'channels/{channel_id}'),
            json=params

        ) as resp:
            assert 200 < resp.status_code < 299