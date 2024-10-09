# Проект 5-го спринта: Автотесты для Stellar Burgers

## Описание

Проект содержит набор автотестов для сайта Stellar Burgers ([https://stellarburgers.nomoreparties.site/](https://stellarburgers.nomoreparties.site/)). Тесты охватывают следующие функциональные области:

- **Авторизация:**
    - Проверка авторизации через Личный кабинет.
    - Проверка авторизации через главную страницу.
    - Проверка авторизации через форму регистрации.
    - Проверка авторизации через форму восстановления пароля.
- **Конструктор:**
    - Проверка переключения между секциями "Соусы", "Начинки", "Булки".
- **Выход из аккаунта:**
    - Проверка выхода из аккаунта.
- **Регистрация:**
    - Проверка успешной регистрации.
    - Проверка регистрации с некорректным паролем.
- **Действия пользователя:**
    - Проверка перехода в личный кабинет.
    - Проверка перехода из личного кабинета в конструктор.
    - Проверка клика по кнопке "Конструктор" и по логотипу.

## Структура проекта

Проект имеет следующую структуру:

### Папка `tests`

- **`test_user_actions.py`:** Тесты для проверки действий пользователя (вход, выход, переходы).
- **`test_constructor_sections.py`:** Тесты для проверки переключения между секциями "Соусы", "Начинки", "Булки".
- **`test_log_out.py`:** Тест для проверки выхода из аккаунта.
- **`test_registration.py`:** Тесты для проверки регистрации.
- **`test_authorization.py`:** Тесты для проверки авторизации.


### Вспомогательные файлы

- **`conftest.py`:**  Содержит фикстуры для WebDriver и данных авторизации.
- **`helper.py`:** Содержит функции по генерации данных (имя, почта, пароль).
- **`Locators.py`:**  Хранит все локаторы для элементов сайта.
- **`pytest.ini`:**  Настройки для pytest.

## Запуск тестов

Для запуска тестов выполните следующую команду из консоли:

```bash
pytest