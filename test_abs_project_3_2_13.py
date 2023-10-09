import unittest    # модуль для создания и запуска тестов.
from selenium import webdriver    # модуль Selenium для управления браузером.
from selenium.webdriver.common.by import By    # модуль Selenium для выбора элементов на веб-странице.
import time    # модуль Python для работы с временными задержками.

class TestRegistration(unittest.TestCase):    # В этом классе будут определены методы для тестирования.

    # Определены два метода для тестов 'test_registration1' и 'test_registration2'
    # Внутри каждого метода выполняется тестирование определенной страницы регистрации.
    def test_registration1(self):    # Каждый метод начинается с 'test_'
        # Внутри каждого метода выполняется следующая последовательность действий:
        link = "http://suninjuly.github.io/registration1.html"    # Задается URL-адрес страницы регистрации:
        browser = webdriver.Chrome()    # Создается экземпляр браузера (в данном случае, Chrome):
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, f"[placeholder='Input your first name']")    # На странице находятся и заполняются обязательные поля формы с использованием метода 'find_element' и 'send_keys'
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, f"[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, f"[placeholder='Input your email']")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")    # Нажимается на кнопку "Submit"
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

        time.sleep(10)
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, f"[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, f"[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, f"[placeholder='Input your email']")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    unittest.main()