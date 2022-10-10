from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

'''
Скрол до чего-либо:
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

Скрол на конкретное количество пикселей:
browser.execute_script("window.scrollBy(0, 100);")
'''

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # GIVEN
    browser.get('http://SunInJuly.github.io/execute_script.html')

    # WHEN
    num = browser.find_element(By.ID, 'input_value').text
    result = calc(str(num))

    text_field = browser.find_element(By.ID, 'answer')
    # browser.execute_script('return arguments[0].scrollIntoView(true);', text_field)
    text_field.send_keys(result)

    robots_check = browser.find_element(By.ID, 'robotCheckbox')
    robots_check.click()

    robots_rule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robots_rule)
    robots_rule.click()

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()
