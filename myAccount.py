from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

username = "andreww52"
password = "test1234"

driver = webdriver.Chrome()


driver.get("https://nj.myaccountqa.pseg.com/user/login")
element = driver.find_element_by_id("username")
element.send_keys(username)
element = driver.find_element_by_id("password")
element.send_keys(password)

print("Page URL: "+driver.current_url)
print("Page title: "+driver.title)
element.send_keys(Keys.RETURN)
# element.close()
