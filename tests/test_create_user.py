import pytest
import allure
from api import StellarBurgersAPI
from helpers import generate_user_data


@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Cоздать уникального пользователя")
    def test_create_unique_user(self, user):
        response = user.get("response")
        assert response.json().get("success")
        assert response.ok

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_existing_user(self, user):
        user_data = user.get("user_data")
        response = StellarBurgersAPI.register_user(user_data)
        assert not response.json().get("success")
        assert response.json().get("message") == "User already exists"
        assert not response.ok
        assert response.status_code == 403

    @allure.title("Cоздать пользователя и не заполнить одно из обязательных полей.")
    @pytest.mark.parametrize("keys", [("email", "password"), ("name", "password")])
    def test_create_user_with_invalid_data(self, keys, test_user):
        response = StellarBurgersAPI.register_user(
            {keys[0]: test_user[keys[0]], keys[1]: test_user[keys[1]]}
        )
        assert not response.json().get("success")
        assert (
            response.json().get("message")
            == "Email, password and name are required fields"
        )
        assert not response.ok
        assert response.status_code == 403
