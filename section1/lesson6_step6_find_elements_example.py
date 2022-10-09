'''
find_elementsб в отличие от find_element, вернёт список всех найденных элементов по заданному условию
Проверив длину списка, мы можем удостовериться, что в корзине отобразилось правильное количество товаров
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://fake-shop.com/book1.html")  # Открываем страницу первого товара

add_button = browser.find_element(By.CSS_SELECTOR, ".add")  # Добавляем товар в корзину
add_button.click()

browser.get("https://fake-shop.com/book2.html")  # Открываем страницу второго товара

add_button = browser.find_element(By.CSS_SELECTOR, ".add")  # Добавляем товар в корзину
add_button.click()

browser.get("https://fake-shop.com/basket.html")  # Открываем корзину

goods = browser.find_elements(By.CSS_SELECTOR, ".good")  # Ищем все добавленные товары

assert len(goods) == 2  # Проверяем, что количество товаров равно 2
