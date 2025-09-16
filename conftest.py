import pytest

from api import StellarBurgersAPI
from helpers import generate_user_data


@pytest.fixture()
def test_user():
    return generate_user_data()


@pytest.fixture()
def user():
    test_user = generate_user_data()
    StellarBurgersAPI.register_user(test_user)
    response = StellarBurgersAPI.login_user(test_user["email"], test_user["password"])
    accessToken = response.json().get("accessToken")
    yield {"response": response, "accessToken": accessToken, "user_data": test_user}
    StellarBurgersAPI.delete_user(accessToken)
