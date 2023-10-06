from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элементы с числами и считаем их сумму
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num1 = int(num1_element.text)  # Затем мы извлекаем текст из найденных элементов и преобразуем его в целые числа.
    num2 = int(num2_element.text)  # Затем мы извлекаем текст из найденных элементов и преобразуем его в целые числа.
    total = num1 + num2  # Вычисляем сумму чисел и сохраняем ее в переменную total.

    # Выбираем значение в выпадающем списке, равное расчетной сумме
    select_element = Select(browser.find_element(By.TAG_NAME, "select"))  #Мы находим выпадающий список (элемент с тегом "select") с помощью find_element(By.TAG_NAME, "select").
    select_element.select_by_value(str(total))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

