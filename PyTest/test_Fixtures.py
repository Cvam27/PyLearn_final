import pytest


@pytest.fixture
def main_url():
    url = "www.google.com"
    return url


def check_url():
    assert main_url == "google"
