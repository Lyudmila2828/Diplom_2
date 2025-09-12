import allure

from api import StellarBurgersAPI
from helpers import generate_user_data


@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.title("Вход под существующим пользователем")
    def test_login_with_correct_credentials(self):
        test_user = generate_user_data()
        response = StellarBurgersAPI.register_user(test_user)
        StellarBurgersAPI.login_user(test_user['email'], test_user['password'])
        assert response.json().get("success")
        assert response.ok

    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_incorrect_credentials(self):
        test_user = generate_user_data()
        response = StellarBurgersAPI.login_user(test_user['email'], test_user['password'])
        assert not response.ok
        assert response.status_code == 401
        assert not response.json().get("success")
        assert response.json().get('message') == 'email or password are incorrect'
