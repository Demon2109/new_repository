
"""Регистрация аккаунта"""
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# myaccount_tab = driver.find_element_by_id("menu-item-50")
# myaccount_tab.click()
# email_field = driver.find_element_by_id("reg_email")
# email_field.send_keys("kazaryan_artur@list.ru")
# password_field = driver.find_element_by_id("reg_password")
# password_field.send_keys("ilovemyparents51777786")
# register_button = driver.find_element_by_css_selector("[value = 'Register']")
# register_button.click()
# time.sleep(1)
#
# driver.quit()

"""Логин в систему"""

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
# logout_element = WebDriverWait(driver, 5).until (EC.presence_of_element_located((By.CSS_SELECTOR , ".woocommerce-MyAccount-navigation li:nth-child(6)>a")))
#
# time.sleep(1)
#
# driver.quit()



