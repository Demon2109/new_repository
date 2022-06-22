"""Отображение страницы товара и проверка названия книги"""

# import time
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# myaccount_tab = driver.find_element_by_id("menu-item-50")
# myaccount_tab.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("kazaryan_artur@list.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("ilovemyparents51777786")
# login_button = driver.find_element_by_css_selector("[value = 'Login']")
# login_button.click()
# time.sleep(1)
# shop_tab = driver.find_element_by_css_selector("#main-nav li:nth-child(1)")
# shop_tab.click()
# HTML5forms_tab = driver.find_element_by_css_selector(".post-181 h3")
# HTML5forms_tab.click()
# text_element = WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.CLASS_NAME, 'product_title'), 'HTML5 Forms'))

# driver.quit()

"""Отображение количества товара"""

# import time
# from selenium import webdriver
#
#
# driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# myaccount_tab = driver.find_element_by_id("menu-item-50")
# myaccount_tab.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("kazaryan_artur@list.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("ilovemyparents51777786")
# login_button = driver.find_element_by_css_selector("[value = 'Login']")
# login_button.click()
# time.sleep(1)
# shop_tab = driver.find_element_by_css_selector("#main-nav li:nth-child(1)")
# shop_tab.click()
# html_tab = driver.find_element_by_css_selector(".product-categories li:nth-child(2)>a")
# html_tab.click()
# number_of_goods = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(number_of_goods) == 3:
#     print("ok")
# else:
#     print("false")


"""Сортировка товара"""
# import time
# from selenium import webdriver
#
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# myaccount_tab = driver.find_element_by_id("menu-item-50")
# myaccount_tab.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("kazaryan_artur@list.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("ilovemyparents51777786")
# login_button = driver.find_element_by_css_selector("[value = 'Login']")
# login_button.click()
# time.sleep(1)
# shop_tab = driver.find_element_by_css_selector("#main-nav li:nth-child(1)")
# shop_tab.click()
# sorting_element = driver.find_element_by_class_name("orderby")
# select = Select(sorting_element)
# select.select_by_value("menu_order")
# sorting_element_default = sorting_element.get_attribute("value")
# select.select_by_value("price-desc")
# sorting_element = driver.find_element_by_class_name("orderby")
# sorting_element_price_desc = sorting_element.get_attribute("value")

"""Отображение, скидка товара"""
# import time
# from selenium import webdriver

# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")

# myaccount_tab = driver.find_element_by_id("menu-item-50")
# myaccount_tab.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("kazaryan_artur@list.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("ilovemyparents51777786")
# login_button = driver.find_element_by_css_selector("[value = 'Login']")
# login_button.click()
# shop_tab = driver.find_element_by_css_selector("#main-nav li:nth-child(1)")
# shop_tab.click()
# android_quick_book = driver.find_element_by_css_selector(".post-169 a:nth-child(1)")
# android_quick_book.click()
#
# """Проверка соответствия старой цены и новой"""
# book_old_price = driver.find_element_by_css_selector(".price>del>span")
# book_old_price.get_text = book_old_price.text
# assert book_old_price.get_text == "₹600.00"
#
# book_new_price = driver.find_element_by_css_selector(".price>ins>span")
# book_new_price.get_text = book_new_price.text
# assert book_new_price.get_text == "₹450.00"
#
# """Проверка того что обложка кликабельна и нажать на нее"""
#
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.images>a')))
# book_cover.click()
#
# book_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# book_cover_close.click()
# time.sleep(2)
# driver.quit()

"""Проверка цены в корзине"""

# from selenium import webdriver

# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# shop_tab = driver.find_element_by_css_selector("#main-nav li:nth-child(1)")
# shop_tab.click()
# HTML5_webdev_book = driver.find_element_by_class_name("post-182")
# HTML5_webdev_book.click()
# add_to_basket_button = driver.find_element_by_class_name("single_add_to_cart_button ")
# add_to_basket_button.click()
#
# """Проверка соответствия цены и суммы рядом с вкладкой корзина"""
# item_element_quantity = driver.find_element_by_class_name("cartcontents")
# item_element_quantity.get_text = item_element_quantity.text
# assert item_element_quantity.get_text == "1 Item"
#
# item_element_ammount = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# item_element_ammount.get_text = item_element_ammount.text
# assert item_element_ammount.get_text == "₹180.00"
#
# cart_tab = driver.find_element_by_id("wpmenucartli")
# cart_tab.click()
#
# """Проверка отображения стоимости в Subtotal и Total в корзине"""
#
# subtotal_field = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal>td'), '₹180.00'))
# total_field = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total>td'), '₹189.00'))

"""Работа в корзине"""
# import time

# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# shop_tab = driver.find_element_by_css_selector("#main-nav li:nth-child(1)")
# shop_tab.click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 300);")
# HTML5_webdev_book = driver.find_element_by_css_selector("[data-product_id = '182']")
# HTML5_webdev_book.click()
# time.sleep(3)
# js_data_structures_book = driver.find_element_by_css_selector("[data-product_id = '180']")
# js_data_structures_book.click()
# time.sleep(2)
# cart_tab = driver.find_element_by_id("wpmenucartli")
# cart_tab.click()
# time.sleep(1)
# delete_first_book_button = driver.find_element_by_css_selector("[data-product_id = '182']")
# delete_first_book_button.click()
# time.sleep(2)
# undo_tab = driver.find_element_by_link_text("Undo?")
# undo_tab.click()
# time.sleep(2)
#
# quantity_of_goods_field = driver.find_element_by_css_selector("tbody>tr:nth-child(1) .product-quantity input")
# quantity_of_goods_field.clear()
# time.sleep(2)
# quantity_of_goods_field.send_keys(3)
# update_basket_button = driver.find_element_by_css_selector("[value = 'Update Basket']")
# update_basket_button.click()
# time.sleep(5)
# quantity_of_goods_field = driver.find_element_by_css_selector("tbody>tr:nth-child(1) .product-quantity input")
# quantity_of_goods_field_value = quantity_of_goods_field.get_attribute("value")
# assert quantity_of_goods_field_value == '3'
# time.sleep(2)
# apply_coupon_button = driver.find_element_by_css_selector("[name = 'apply_coupon']")
# apply_coupon_button.click()
# text_element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error>li'), 'Please enter a coupon code.'))
#
# driver.quit()

"""Покупка товара"""
import time
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")

driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

shop_tab = driver.find_element_by_css_selector("#main-nav li:nth-child(1)")
shop_tab.click()
driver.execute_script("window.scrollBy (0, 300);")

HTML5_webdev_book = driver.find_element_by_css_selector("[data-product_id = '182']")
HTML5_webdev_book.click()
time.sleep(2)
cart_tab = driver.find_element_by_id("wpmenucartli")
cart_tab.click()
proceed_to_checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button'))).click()
first_name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))
first_name_field.send_keys("Arthur")
last_name_field = driver.find_element_by_id("billing_last_name")
last_name_field.send_keys("Kazaryan")
email_field = driver.find_element_by_id("billing_email")
email_field.send_keys("kazaryan_artur@list.ru")
phone_field = driver.find_element_by_id("billing_phone")
phone_field.send_keys("89260430112")

time.sleep(2)
select_element_county = driver.find_element_by_class_name("select2-container").click()
select_element_field = driver.find_element_by_class_name("select2-input")
select_element_field.send_keys("Ger")

driver.find_element_by_css_selector("").click()

steet_address_field = driver.find_element_by_id("billing_address_1")
steet_address_field.send_keys("ulmen strasse,26")
city_field = driver.find_element_by_id("billing_city")
city_field.send_keys("hamburg")
# state_country_field = driver.find_element_by_id("billing_state")
# state_country_field.send_keys("dakota")
postcode_field = driver.find_element_by_id("billing_postcode")
postcode_field.send_keys("22245")
driver.execute_script("window.scrollBy (0, 600);")
time.sleep(2)
payment_method_checkbox = driver.find_element_by_css_selector(".wc_payment_methods>li:nth-child(2) input")
payment_method_checkbox.click()
driver.find_element_by_id("place_order").click()
text_element = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received'))
payment_method_text = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element,((By.CSS_SELECTOR, '.method>strong'), 'Check Payments'))

