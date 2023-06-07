import pytest
from selene.support.shared import config

@pytest.fixture(autouse = True)
def setup_browser():
    config.timeout = 10
    config.window_width = 400
    config.window_height = 400
    config.base_url = 'https://www.google.com/ncr'

    yield