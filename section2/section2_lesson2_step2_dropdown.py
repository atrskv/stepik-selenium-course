'''
У каждого элемента списка обычно есть уникальное значение атрибута value

Есть удобный способ, для которого используется специальный класс Select из библиотеки WebDriver

Сначала мы должны инициализировать новый объект, передав в него WebElement с тегом select
Далее можно найти любой вариант из списка с помощью метода select_by_value(value):

# from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element(By.TAG_NAME, "select"))
# select.select_by_value("1") # ищем элемент с текстом "Python"

Можно использовать еще два метода: select.select_by_visible_text("text") и
select.select_by_index(index)

Первый способ ищет элемент по видимому тексту, например,
select.select_by_visible_text("Python") найдёт "Python"

Второй способ ищет элемент по его индексу или порядковому номеру
Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python",
нужно использовать select.select_by_index(1), так как опция с индексом 0 в данном
примере имеет значение по умолчанию равное "--"
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    # GIVEN
    browser.get('http://suninjuly.github.io/selects2.html')

    # WHEN
    first_num_value = float(browser.find_element(By.ID, 'num1').text)
    second_num_value = float(browser.find_element(By.ID, 'num2').text)

    sum = int(first_num_value + second_num_value)

    dropdown = Select(browser.find_element(By.ID, 'dropdown'))
    dropdown.select_by_value(str(sum))

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()