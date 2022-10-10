from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

# GIVEN
try:
    browser.get('https://suninjuly.github.io/math.html')

# WHEN
    x_value = browser.find_element(By.ID, 'input_value').text
    result = calc(x_value)

    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(result)

    people_check = browser.find_element(By.ID, 'robotCheckbox')
    people_check.click()

    people_radiobutton = browser.find_element(By.ID, 'peopleRule')
    robots_radiobutton = browser.find_element(By.ID, 'robotsRule')

    # THEN
    people_checked = people_radiobutton.get_attribute('checked')
    robots_checked = robots_radiobutton.get_attribute('checked')

    robots_radiobutton.click()
    # people_radiobutton.click()

    # Если ничего нет, get_attribute возвращает none, если есть - true (с маленькой буквы)
    assert people_checked == 'true', 'FALSE'

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
