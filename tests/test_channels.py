# -*- coding: UTF-8 -*-
from __future__ import print_function
'''
Channel api testing
'''

from pprint import pprint

def test_list_channels(api):
    channels = api.Channels.getChannels().response().result
    assert len(channels) > 0
    assert channels[0]['id'] > 0

# def test_interact_with_shutter(api, SHUTTER_ID):
#     ActionRequest = api.Channels.get_model('ChannelExecuteActionRequest')
#     pprint(
#         api
#         .Channels
#         .executeAction(id=SHUTTER_ID, body=ActionRequest(action='REVEAL'))
#         .response().result
#     )