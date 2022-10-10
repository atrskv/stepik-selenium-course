'''
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()

message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

Во время поиска WebDriver каждые 0.5 секунды проверяет, появился ли нужный элемент в DOM-модели браузера
'''

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")
'''

'''
Еще больше правил из EC:
- title_is
- title_contains
- presence_of_element_located
- visibility_of_element_located
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_clickable
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present
'''

'''
Общее:
http://chromedriver.chromium.org/getting-started﻿
﻿https://www.guru99.com/selenium-tutorial.html — ﻿Туториал на английском, ориентирован на Java.﻿
https://www.guru99.com/live-selenium-project.html — ﻿Можно попробовать писать автотесты для демо-сайта ﻿банка. Тоже Java.
http://barancev.github.io/good-locators/ — что такое хорошие селекторы
http://barancev.github.io/what-is-path-env-var/ — что за PATH переменная? 

Ожидания в Selenium WebDriver:
https://www.selenium.dev/documentation/webdriver/waits/﻿﻿
https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
https://blog.codeship.com/get-selenium-to-wait-for-page-load/
http://barancev.github.io/slow-loading-pages/
http://barancev.github.io/page-loading-complete/

Git:
https://learngitbranching.js.org/ — отличный интерактивный туториал
https://git-scm.com/book/ru/v2/ — лучшая книга
https://hyperskill.org/learn/topic/257/﻿
https://stepik.org/course/4138/﻿
https://stepik.org/course/3145/
http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html
https://habr.com/company/intel/blog/344962/
https://githowto.com/ru
'''

from selenium import webdriver
import time
import math

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def calc(x: str):
    return math.log(abs(12*math.sin(int(x))))


try:
    # GIVEN
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # WHEN
    price = (WebDriverWait(browser, 12)
             .until(expected_conditions
                    .text_to_be_present_in_element((By.ID, 'price'), '$100')))  # Ждем спада цены

    button = browser.find_element(By.ID, "book")
    button.click()


    num = browser.find_element(By.ID, 'input_value').text
    result = calc(num)


    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(result)

    submit = browser.find_element(By.ID, 'solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
