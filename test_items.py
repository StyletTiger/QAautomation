from selenium.webdriver.common.by import By

# Установим желаемый язык, например, испанский
user_language = "es"



# Укажим URL-адрес для вашего теста
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
