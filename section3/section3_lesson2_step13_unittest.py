from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

'''
Для unittest существуют собственные дополнительные правила:
- тесты обязательно должны находиться в специальном тестовом классе.
- вместо assert должны использоваться специальные assertion методы.
'''

# python3 section3_lesson2_step13_unittest.py

class TestRegistration(unittest.TestCase):  # Cоздаем класс, который наследуется от TestCase

    def test_registration_should_pass(self):  # Делаем из функций методы, ссылаясь на self

        # GIVEN
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # WHEN
        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_name.send_keys('Aleksei')

        second_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        second_name.send_keys('Torsukov')

        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email.send_keys('email@email.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # THEN
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, 'Should be equel')  # Исправляем ассерт

        browser.quit()

    def test_registration_should_fail(self):

        # GIVEN
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # WHEN
        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_name.send_keys('Aleksei')

        second_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        second_name.send_keys('Torsukov')

        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email.send_keys('email@email.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # THEN
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, 'Should be equel')

        browser.quit()


if __name__ == "__main__":
    unittest.main()  # Заменяем запуск





pytest scripts/selenium_scripts
# найти все тесты в директории scripts/selenium_scripts

pytest test_user_interface.py
# найти и выполнить все тесты в файле 

pytest scripts/drafts.py::test_register_new_user_parametrized
# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить 

все тесты, название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)
для пайтеста


Если запустить PyTest с параметром -v (verbose, то есть подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения: 

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"
    
    pytest test_abs.py

Если вы используете unittest, то для проверки ожидаемых результатов в тестах вам нужно знать и использовать большой набор assert-методов, например, таких: assertEqual, assertNotEqual, assertTrue, assertFalse и другие.

В PyTest используется стандартный assert метод из языка Python, что делает код более очевидным.

unittest:

self.assertEqual(a, b, msg="Значения разные")
PyTest:

assert a == b, "Значения разные"


Если нужно проверить, что тест вызывает ожидаемое исключение (довольно редкая ситуация для UI-тестов, и вам этот способ, скорее всего, никогда не пригодится), мы можем использовать специальную конструкцию with pytest.raises(). Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:



import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


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
        
        В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException, которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.





@Дмитрий_Иванов, в данном случае, для того, чтобы передать browser в класс. Можете попробовать запустить без него и посмотреть, что получится.


че делать с фикстурой 

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        
        

финализатор 


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        
        
        Для фикстур можно задавать область покрытия фикстур. Допустимые значения: “function”, “class”, “module”, “session”. Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или один раз для всех тестов, запущенных в данной сессии. 
        
        
        
        
    import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
        
        
        
    При описании фикстуры можно указать дополнительный параметр autouse=True, который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова: 


https://habr.com/ru/company/yandex/blog/242795/

https://docs.pytest.org/en/stable/fixture.html

'''