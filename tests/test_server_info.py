# -*- coding: UTF-8 -*-
from __future__ import print_function
'''
Test Server API
'''
def test_server_info(api):
    server_info = api.get_server_info()
    assert server_info['authenticated'] == True