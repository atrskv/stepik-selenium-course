'''
Фиксируем то, что используем:
pip freeze > requirements.txt

Скачиваем то, что нужно:
pip install -r requirements.txt
'''

# Найти все тесты в директории scripts/selenium_scripts
# pytest scripts/selenium_scripts

# Найти и выполнить все тесты в файле
# pytest test_user_interface.py

# Найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить
# pytest scripts/drafts.py::test_register_new_user_parametrized

# Если запустить PyTest с параметром -v (verbose, то есть подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения

# Если вы используете unittest, то для проверки ожидаемых результатов в тестах вам нужно знать
# и использовать большой набор assert-методов, например, таких: assertEqual, assertNotEqual, assertTrue, assertFalse и другие
# unittest: self.assertEqual(a, b, msg="Значения разные")

# В PyTest используется стандартный assert метод из языка Python, что делает код более очевидным
# PyTest: assert a == b, "Значения разные"


# Если нужно проверить, что тест вызывает ожидаемое исключение, мы можем использовать специальную конструкцию with pytest.raises()
# Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

'''
В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException, 
которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт
'''

def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()
