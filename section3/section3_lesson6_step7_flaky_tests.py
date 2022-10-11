'''
Flaky-тесты или "мигающие" авто-тесты, т.е. такие тесты,
которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов,
могут иногда падать, хотя всё остальное время они проходят успешно

Будем перезапускать упавший тест, чтобы еще раз убедиться, что он действительно нашел баг,
а не упал случайно

Для этого мы будем использовать плагин pytest-rerunfailures

pip3 install pytest-rerunfailures

Чтобы указать количество перезапусков для каждого из упавших тестов,
нужно добавить в командную строку параметр:
"--reruns n", где n — это количество перезапусков

Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста
'''
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

# pytest -v --tb=line --reruns 1 --browser_name=chrome name.py
