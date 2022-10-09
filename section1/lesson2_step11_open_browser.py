'''
Selenium — это проект, который предназначен для автоматизации тестирования веб-приложений

Он состоит из множества самых разных компонентов, например:
- Selenium WebDriver
- Selenium Grid
- Selenium Server
- Selenium IDE

Selenium WebDriver — универсальный интерфейс, который позволяет манипулировать разными браузерами
напрямую из кода на языке программирования

То есть: Python -> Selenium WebDriver -> ChromeDriver -> Google Chrome
'''

import time  # для комфортного просмотра
from selenium import webdriver  # webdriver - набор команд для управления браузером
from selenium.webdriver.common.by import By  # в By находятся способы поиска элемента

driver = webdriver.Chrome()  # инициализируем драйвер браузера


time.sleep(5)


driver.get("https://stepik.org/lesson/25969/step/12")  # с помощью .get открываем сайт


time.sleep(5)


textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")  # find_element позволяет найти нужный элемент на странице
textarea.send_keys("get()")


time.sleep(5)


submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()


time.sleep(5)


driver.quit()
