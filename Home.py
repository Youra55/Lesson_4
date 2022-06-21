# Добавление комментария

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
# Открытие страницы
driver.get("http://practice.automationtesting.in/")
# Скролл вниз
driver.execute_script("window.scrollBy(0, 600);")
# Заполнение данных
driver.find_element_by_css_selector("[data-product_id='160']").click()
driver.find_element_by_css_selector("[class='reviews_tab']").click()
driver.find_element_by_css_selector("[class='star-5']").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Yuriy Chistyakov")
driver.find_element_by_id("email").send_keys("123@mail.ru")
driver.find_element_by_id("submit").click()
driver.quit()