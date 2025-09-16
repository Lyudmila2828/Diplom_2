import allure
from faker import Faker

from api import StellarBurgersAPI

@allure.step('Генерация тестовых данных пользователя')
def generate_user_data():
    fake = Faker()
    email = fake.email()
    name = fake.user_name()
    password = fake.password(8)
    return {"email": email, "password": password, "name": name}
