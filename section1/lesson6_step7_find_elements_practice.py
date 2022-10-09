from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")

    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)  # Для того, чтобы успеть скопировать код из модального окна
    browser.quit()

'''
Тег label используется, чтобы сделать кликабельным текст, который отображается рядом с флажком
Этот текст заключен внутри тега label. Элемент label связывается с элементом input с помощью атрибута for,
в котором указывается значение атрибута id для элемента input
'''