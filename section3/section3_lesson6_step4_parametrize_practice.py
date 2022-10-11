import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)

    yield browser

    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link',
[
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
]
                        )
def test_cooper(browser, link):

    # GIVEN
    browser.get(link)

    # WHEN
    answer = math.log(int(time.time()))

    # text_area = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')


    text_area = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area')))
    text_area.send_keys(answer)


    submit = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    submit.click()

    # THEN

    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text

    # result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    assert result == 'Correct!', 'ALARM!'

 