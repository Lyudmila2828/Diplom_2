import pytest

from helpers import generate_user_data


@pytest.fixture()
def test_user():
    return generate_user_data()