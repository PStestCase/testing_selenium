import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://nj.myaccountqa.pseg.com/user/login")

username = "andreww52"
password = "test1234"
element = driver.find_element_by_id("username")
element.send_keys(username)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
driver.find_element_by_css_selector(
    "input#radioCntAccount650216760800 + label").click()
driver.find_element_by_id("btnSwitchSelectedAccount").click()

driver.implicitly_wait(10)
driver.find_element_by_id('MyAccount').click()
driver.find_element_by_link_text('Billing & Payment History').click()
driver.find_element_by_id('readingBillingItem').click()

