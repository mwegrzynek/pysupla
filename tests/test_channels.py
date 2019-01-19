# -*- coding: UTF-8 -*-
from __future__ import print_function
'''
Channel api testing
'''

def test_list_all_channels(api):
    channels = api.get_channels()
    assert len(channels) > 0
    assert channels[0]['id'] > 0

def test_list_only_shutters(api):
    channels = api.get_channels(func=['CONTROLLINGTHEROLLERSHUTTER'])

    assert len(channels) > 0
    for chan in channels:
        assert chan['function']['name'] == 'CONTROLLINGTHEROLLERSHUTTER'

def test_list_only_shutters_and_light_switches(api):
    channels = api.get_channels(func=['CONTROLLINGTHEROLLERSHUTTER', 'LIGHTSWITCH'])

    assert len(channels) > 0
    for chan in channels:
        assert chan['function']['name'] in ('LIGHTSWITCH', 'CONTROLLINGTHEROLLERSHUTTER')

def test_get_shutter_info(api, SHUTTER_ID):
    shutter = api.get_channel(SHUTTER_ID)
    assert shutter['function']['name'] == 'CONTROLLINGTHEROLLERSHUTTER'

def test_get_shutter_info_with_iodevice_and_state(api, SHUTTER_ID):
    shutter = api.get_channel(SHUTTER_ID, include=('iodevice', 'state'))
    assert 'shut' in shutter['state']

def test_open_shutters(api, SHUTTER_ID):
    api.execute_action(SHUTTER_ID, 'REVEAL')

def test_close_shutters(api, SHUTTER_ID):
    api.execute_action(SHUTTER_ID, 'SHUT')

