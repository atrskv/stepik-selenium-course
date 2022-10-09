'''
Поиск элементов в find_element:
find_element(By.ID, value
find_element(By.CSS_SELECTOR, value)
find_element(By.XPATH, value)
find_element(By.NAME, value)
find_element(By.TAG_NAME, value)
find_element(By.CLASS_NAME, value)
find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице,
если текст селектора совпадает с любой частью текста ссылки.
'''

'''
browser.close() закрывает текущее окно браузера

Если скрипт вызвал всплывающее окно, или открыл что-то в новом окне 
или вкладке браузера, то закроется только текущее окно, а все остальные останутся висеть 

browser.quit() закрывает все окна, вкладки и процессы

Для того, чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, 
проще всего использовать конструкцию try/finally
'''

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    browser.quit()
