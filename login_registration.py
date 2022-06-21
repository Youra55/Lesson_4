# Регистрация аккаунта
#import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver # импортируем webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.implicitly_wait(10)
#driver.get("http://practice.automationtesting.in/")
#driver.find_element_by_id("menu-item-50").click()
#driver.find_element_by_id("reg_email").send_keys("nikotin_4@mail.ru")
#driver.find_element_by_id("reg_password").send_keys("fsdfFRFSDG231245")
#driver.find_element_by_css_selector("[name='register']").click()

# Логин в систему
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("nikotin_4@mail.ru")
driver.find_element_by_id("password").send_keys("fsdfFRFSDG231245")
driver.find_element_by_css_selector("[name='login']").click()
element = driver.find_element_by_css_selector("[class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']")
element_get_text = element.text
assert "Logout" in element_get_text

