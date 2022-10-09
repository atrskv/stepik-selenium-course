from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    # GIVEN
    link = 'http://suninjuly.github.io/registration2.html'
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


    time.sleep(1)


    # THEN
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

