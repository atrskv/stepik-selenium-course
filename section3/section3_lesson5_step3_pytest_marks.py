'''
Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name,
где mark_name — произвольная строка

Например, критичные - smoke, на каждый коммит. Остальное - regression, перед релизом
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# pytest -s -v -m smoke name.py

# Как регистрировать метки?
# pytest.ini, а там:
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests

# Инверсия
# pytest -s -v -m "not smoke" name.py

# Логическое "ИЛИ"
# pytest -s -v -m "smoke or regression" test_fixture8.py

# pytest -s -v -m "smoke and win10" name.py - логическое "И"
@pytest.mark.smoke
@pytest.mark.win10
def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# @pytest.mark.skip - пропуск теста (чтобы не портил результаты, например)
# @pytest.mark.xfail - для заведомо падающего теста (пока чинится баг)

# XPASS (“unexpectedly passing” — неожиданно проходит), когда баг починится и тест пройдет
# После этого маркировку можно будет удалить


import pytest

@pytest.mark.xfail(strict='False')  # Пометит тест упавшим
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False


