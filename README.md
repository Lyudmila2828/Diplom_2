## Дипломный проект. Задание 2: API-тесты
<hr>

## Студент: Симоненкова Людмила

## <h>Когорта: #27</h>
<hr>

## <h>Project: Stellar Burgers API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest tests

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла          | Содержание файла                  |
|-------------------------|-----------------------------------|
| Tests dir               | Директория с тестами              |
| test_create_user.py     | Тесты на создание пользователя    |
| test_login_user.py      | Тесты на регистрацию пользователя |
| test_make_order.py      | Тесты на создание заказа          |
| conftest.py             | Фикстуры                          |
| helpers.py              | Хэлперы                           |
| data.py                 | Файл с URL и эндпоинтами          |
| api.py                  | Методы работы с API               |
| requirements.txt        | Файл с зависимостями              |
| allure-results.dir      | Папка с отчетами Allure           |
