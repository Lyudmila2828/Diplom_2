import allure
import pytest

from api import StellarBurgersAPI
from helpers import generate_user_data


@allure.feature("Создание заказа")
class TestMakeOrder:
    @allure.title("Создание заказа с авторизацией")
    def test_make_order_with_auth(self, user):
        accessToken = user.get("accessToken")
        response = StellarBurgersAPI.create_order(
            ["61c0c5a71d1f82001bdaaa6d"], accessToken
        )
        assert response.ok
        assert response.status_code == 200
        assert response.json().get("success")

    @allure.title("Создание заказа без авторизации")
    def test_make_order_without_auth(self):
        response = StellarBurgersAPI.create_order(["61c0c5a71d1f82001bdaaa6d"])
        assert not response.ok
        assert not response.status_code == 401
        assert not response.json().get("success")

    @pytest.mark.parametrize(
        "ingredients",
        [
            ["61c0c5a71d1f82001bdaaa6d"],
            ["61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa6d"],
        ],
    )
    @allure.title("Создание заказа с ингредиентами")
    def test_make_order_with_ingredients(self, ingredients, user):
        accessToken = user.get("accessToken")
        response = StellarBurgersAPI.create_order(ingredients, accessToken)
        assert response.ok
        assert response.status_code == 200
        assert response.json().get("success")

    @allure.title("Создание заказа без ингредиентов")
    def test_make_order_without_ingredients(self, user):
        accessToken = user.get("accessToken")
        response = StellarBurgersAPI.create_order([], accessToken)
        assert not response.ok
        assert response.status_code == 400
        assert not response.json().get("success")
        assert response.json().get("message") == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    def test_make_order_with_invalid_ingredient_hash(self, user):
        accessToken = user.get("accessToken")
        response = StellarBurgersAPI.create_order(["invalidHash"], accessToken)
        assert not response.ok
        assert response.status_code == 500
