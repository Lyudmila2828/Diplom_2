import allure
import requests
from data import *

BASE_URL = "https://stellarburgers.nomoreparties.site/api"


class StellarBurgersAPI:

    @allure.step("Создание заказа")
    def create_order(ingredients, token=None):
        headers = {"Authorization": f"{token}"} if token else {}
        return requests.post(
            ORDER_URL, json={"ingredients": ingredients}, headers=headers
        )

    @allure.step("Регистрация пользователя")
    def register_user(payload):
        return requests.post(REGISTER_URL, json=payload)

    @allure.step("Авторизация пользователя")
    def login_user(email, password):
        return requests.post(LOGIN_URL, json={"email": email, "password": password})
