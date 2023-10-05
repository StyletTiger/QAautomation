from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    treasure = browser.find_element(By.ID, "treasure")

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи, и посчитать значение для перееменной х.
    treasure2 = treasure.get_attribute("valuex")
    x = treasure2
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input = browser.find_element(By.CSS_SELECTOR, f"[id='answer']")
    input.send_keys(y)

    # Отметить checkbox "I'm the robot".
    input = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    input.click()

    # Выбрать radiobutton "Robots rule!".
    input = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()