from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


class Test():
    # Создаем список ссылок
    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]
    #@pytest.fixture(scope="function")
    @pytest.mark.parametrize("link, links")
    @pytest.mark.smoke
    def test_3_6_5(browser, link):
        link = "https://stepik.org/lesson/236895/step/1"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.implicitly_wait(5)

        button = browser.find_element(By.ID, "ember33")
        button.click()

        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("stylettiger3004@gmail.com")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("vodwok-bewbe5-wAvzuq")

        button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
        button.click()


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()