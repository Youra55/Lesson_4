# Отображение страницы товара

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# # Открыли главную страницу
# driver.get("http://practice.automationtesting.in/")
# # Логинимся
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("nikotin_4@mail.ru")
# driver.find_element_by_id("password").send_keys("fsdfFRFSDG231245")
# driver.find_element_by_css_selector("[name='login']").click()
# # Вкладка Shop
# driver.find_element_by_id("menu-item-40").click()
# # Книга "HTML 5 Forms"
# driver.find_element_by_css_selector("[alt='Mastering HTML5 Forms']").click()
# # Проверка что название книги "HTML 5 Forms"
# element = driver.find_element_by_css_selector("[class='product_title entry-title']")
# element_get_text = element.text
# assert "HTML5 Forms" in element_get_text
# driver.quit()

# Количество товаров в категории

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://practice.automationtesting.in/")
# # Логинимся
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("nikotin_4@mail.ru")
# driver.find_element_by_id("password").send_keys("fsdfFRFSDG231245")
# driver.find_element_by_css_selector("[name='login']").click()
# driver.find_element_by_id("menu-item-40").click() # Вкладка Shop
# # Категория HTML
# driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']").click()
# # Проверка, что в категории 3 книги
# items_count = driver.find_elements_by_css_selector('[class="price"]')
# if len(items_count) == 3:
#     print("В разделе 3 книги")
# else:
#     print("Ошибка. Количество книг в разделе: " + str(len(items_count)))
# driver.quit()

# Сортировка товара

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# # Открытие страницы
# driver.get("http://practice.automationtesting.in/")
# # Логинимся
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("nikotin_4@mail.ru")
# driver.find_element_by_id("password").send_keys("fsdfFRFSDG231245")
# driver.find_element_by_css_selector("[name='login']").click()
# # Переключаемся на вкладку Shop
# driver.find_element_by_id("menu-item-40").click() # Вкладка Shop
# # Проверка вариант сортировки по умолчанию
# element = driver.find_element_by_css_selector("[value='menu_order']")
# element_check = element.get_attribute("selected")
# print("Вариант по умолчанию: ", element_check)
# element_check = element.get_attribute("value")
# assert element_check == "menu_order"
# # Выбираем вариант от большего к меньшему
# element2 = driver.find_element_by_css_selector("[class='orderby']")
# select = Select(element2)
# select.select_by_value("price-desc")
# time.sleep(3)
# # Снова объявляем переменную
# element2 = driver.find_element_by_css_selector("[value='price-desc']")
# # Проверка, что выбран вариант от большего к меньшему
# element_check2 = element2.get_attribute("selected")
# print("Вариант от большего к меньшему: ", element_check2)
# element_check2 = element2.get_attribute("value")
# assert element_check2 == "price-desc"
# driver.quit()


# Отображение, скидка товара

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# # Открытие страницы
# driver.get("http://practice.automationtesting.in/")
# # Логинимся
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("nikotin_4@mail.ru")
# driver.find_element_by_id("password").send_keys("fsdfFRFSDG231245")
# driver.find_element_by_css_selector("[name='login']").click()
# # Переключаемся на вкладку Shop
# driver.find_element_by_id("menu-item-40").click() # Вкладка Shop
# # Открываем книгу "Android Quick Start Guide"
# driver.find_element_by_css_selector(".post-169 h3").click()
# # тест, что содержимое старой цены = "₹600.00"
# price1 = driver.find_element_by_css_selector("[class='price']>del>span")
# price1_text = price1.text
# assert price1_text == "₹600.00"
# # тест, что содержимое новой цены = "₹450.00"
# price2 = driver.find_element_by_css_selector("[class='price']>ins>span")
# price2_text = price2.text
# assert price2_text == "₹450.00"
# # Явное ожидание для обложки книги
# imagine = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# imagine.click()
# # Явное ожидание для кнопки закрытия
# button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='pp_close']")))
# button.click()
# driver.quit()


# Проверка цены в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# # Открытие страницы
# driver.get("http://practice.automationtesting.in/")
# # Переключаемся на вкладку Shop
# driver.find_element_by_id("menu-item-40").click() # Вкладка Shop
# # Скролл вниз
# driver.execute_script("window.scrollBy(0, 600);")
# # Добавили книгу в корзину "HTML5 WebApp Development"
# driver.find_element_by_css_selector("[data-product_id='182']").click()
# # тест, что количество товаров = "1 Item"
# time.sleep(2)
# price1 = driver.find_element_by_css_selector("[class='cartcontents']")
# price1_text = price1.text
# assert price1_text == "1 Item"
# # тест, что стоимость = "₹180.00"
# price2 = driver.find_element_by_css_selector("[class='amount']")
# price2_text = price2.text
# assert price2_text == "₹180.00"
# # Переход в корзину
# price2.click()
# # Явное ожидание, что в Subtotal отобразилась стоимость
# some_element= WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']>:nth-child(1)"), "₹180.00"))
# # Явное ожидание, что в Total отобразилась стоимость
# some_element2= WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='order-total']>td>strong>span"), "₹189.00"))
# driver.quit()


# Работа в корзине
#
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# # Открытие страницы
# driver.get("http://practice.automationtesting.in/")
# # Переключаемся на вкладку Shop
# driver.find_element_by_id("menu-item-40").click() # Вкладка Shop
# # Скролл вниз
# driver.execute_script("window.scrollBy(0, 600);")
# # Добавили книги в корзину "HTML5 WebApp Development" "JS Data Structures and Algorithm"
# driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 1000);")
# driver.find_element_by_css_selector("[data-product_id='180']").click()
# # Переход в корзину
# driver.find_element_by_css_selector("[class='cartcontents']").click()
# # Удаляем первую книгу
# time.sleep(3)
# driver.find_element_by_css_selector("[data-product_id='182']").click()
# # Отмена удаления
# driver.find_element_by_link_text("Undo?").click()
# # Увеличение количества товара до 3х шт
# driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
# driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").send_keys('3')
# driver.find_element_by_css_selector("[name='cart[4c5bde74a8f110656874902f07378009][qty]']").clear()
# driver.find_element_by_css_selector("[name='cart[4c5bde74a8f110656874902f07378009][qty]']").send_keys('3')
# # Нажмем кнопку 'Update Basket'
# driver.find_element_by_css_selector("[value='Update Basket']").click()
# #  Тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# element = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# element_check = element.get_attribute("value")
# assert element_check == "3"
# # Нажмем кнопку "APPLY COUPON"
# time.sleep(3)
# driver.find_element_by_css_selector("[name='apply_coupon']").click()
# # тест, что возникло сообщение: "Please enter a coupon code."
# error = driver.find_element_by_css_selector("[class='woocommerce-error']")
# error_text = error.text
# assert error_text == "Please enter a coupon code."
# driver.quit()


# Покупка товара

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
# Открытие страницы
driver.get("http://practice.automationtesting.in/")
# Переключаемся на вкладку Shop
driver.find_element_by_id("menu-item-40").click() # Вкладка Shop
# Скролл вниз
driver.execute_script("window.scrollBy(0, 600);")
# Добавили книгу в корзину "HTML5 WebApp Development"
driver.find_element_by_css_selector("[data-product_id='182']").click()
# Переход в корзину
time.sleep(2)
driver.find_element_by_css_selector("[class='cartcontents']").click()
# Кнопка "PROCEED TO CHECKOUT" с явным ожиданием
button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='checkout-button button alt wc-forward']")))
driver.find_element_by_css_selector("[class='checkout-button button alt wc-forward']").click()
# Заполнение обязательных полей
button1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
driver.find_element_by_id("billing_first_name").send_keys("Youra")
driver.find_element_by_id("billing_last_name").send_keys("Chistyakov")
driver.find_element_by_id("billing_email").send_keys("nikotin_4@mail.ru")
driver.find_element_by_id("billing_phone").send_keys("+79249379992")
driver.find_element_by_id("s2id_billing_country").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
driver.find_element_by_id("select2-results-1").click()
driver.find_element_by_id("billing_address_1").send_keys("Portugalskaya")
driver.find_element_by_id("billing_city").send_keys("Omsk")
driver.find_element_by_id("billing_state").send_keys("Omskaya")
driver.find_element_by_id("billing_postcode").send_keys("644077")
# способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_id("payment_method_cheque").click()
# Нажать кнопку place_order
driver.find_element_by_id("place_order").click()
# Проверка, что отображается "Thank you. Your order has been received."
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received."))
# Проверка, что в Payment Method отображается текст "Check Payments"
some_element2= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='method']"), "Check Payments"))
driver.quit()


