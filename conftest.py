import pytest
from selene.support.shared import config

@pytest.fixture(autouse = True)
def setup_browser():
    config.timeout = 10
    config.window_width = 800
    config.window_height = 600
    config.base_url = 'https://www.google.com/ncr'

    yield