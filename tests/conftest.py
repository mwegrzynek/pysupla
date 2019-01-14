# -*- coding: UTF-8 -*-
import pytest
import os


@pytest.fixture
def SERVER():
    return os.environ['SUPLA_SERVER']

@pytest.fixture
def PERSONAL_ACCESS_TOKEN():
    return os.environ['SUPLA_PERSONAL_ACCESS_TOKEN']

@pytest.fixture
def api(SERVER, PERSONAL_ACCESS_TOKEN):
    from pysupla import PySuplaAPI

    return PySuplaAPI(
        server=SERVER,
        personal_access_token=PERSONAL_ACCESS_TOKEN
    )