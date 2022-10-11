'''
Чтобы указать язык браузера с помощью WebDriver,
используйте класс Options и метод add_experimental_option, как указано в примере ниже:

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

###########################################################

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)

Если сервер получит запрос с заголовком {accept-language: ru, en},
то он отобразит пользователю русскоязычный интерфейс сайта
'''