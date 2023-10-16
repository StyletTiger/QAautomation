import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавим обработчик для параметра language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Specify user language')


# В фикстуре browser используем параметр language для настройки языка браузера
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')

    # Создаём объект опций браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Запускаем браузер с настроенными опциями
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()
