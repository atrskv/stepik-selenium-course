import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestCataloge:

    def test_the_product_button_is_visible(self, browser):

        # GIVEN
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

        # THEN
        product_button = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))

        time.sleep(10)  # For review

        assert product_button, 'There is no button!'

