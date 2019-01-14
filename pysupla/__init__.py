# -*- coding: UTF-8 -*-
from __future__ import print_function

import os.path
import sys
import warnings


from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file

from requests.compat import urljoin, urlsplit


# For bravado
warnings.filterwarnings("ignore", module="collections.*")


def PySuplaAPI(server, personal_access_token):
    http_client = RequestsClient()
    http_client.set_api_key(
        server, 
        'Bearer {}'.format(personal_access_token),
        param_name='Authorization', param_in='header'
    )

    spec_path = os.path.join(
        os.path.dirname(sys.modules['pysupla'].__file__),
        'swagger.json'
    )

    spec = load_file(spec_path)
    spec['host'] = server

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        
        client = SwaggerClient.from_spec(
            spec,
            origin_url='https://{}'.format(server),
            http_client=http_client,
            config=dict(validate_responses=False)
        )

    return client

