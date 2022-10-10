'''
Переключиться на другую вкладку:
browser.switch_to.window(window_name)

Узнать имя вкладки. Открылось всего две - берем имя второй:
new_window = browser.window_handles[1]

Запоминаем имя вкладки:
first_window = browser.window_handles[0]
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()

def calc(x: str):
    return math.log(abs(12*math.sin(int(x))))

try:
    # GIVEN
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    # WHEN
    button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
    button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)


    num = browser.find_element(By.ID, 'input_value').text
    result = calc(num)


    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(result)

    answer_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    answer_button.click()

finally:
    time.sleep(10)
    browser.quit()
