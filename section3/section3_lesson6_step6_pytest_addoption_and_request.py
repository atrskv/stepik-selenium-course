# pytest -s -v --browser_name=firefox test_cmd.py
# /usr/local/bin
# % brew install geckodriver

'''
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")
'''
from selenium.webdriver.common.by import By

'''
Можно настраивать тестовые окружения с помощью передачи параметров через командную строку

Это делается с помощью встроенной функции pytest_addoption и фикстуры request


Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption, 
затем напишем фикстуру, которая будет обрабатывать переданные в опции данные

Добавим логику обработки командной строки в conftest.py
Для запроса значения параметра мы можем вызвать команду:
browser_name = request.config.getoption("browser_name")
'''

# CONFTEST.PY
# import pytest
# from selenium import webdriver
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     #browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# TEST
link = "http://selenium1py.pythonanywhere.com/"



def test_guest_should_see_login_link(browser):

    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


# Если "pytest -s -v test_parser.py", то будет ошибка, параметр не передан
# Можно задать параметр по умолчанию

# parser.addoption('--browser_name', action='store', default="chrome",
#                help="Choose browser: chrome or firefox")

# pytest -s -v --browser_name=firefox test_parser.py
