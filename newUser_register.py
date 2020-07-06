from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://nj.myaccountqa.pseg.com/user/login")

firstName = "ADRIANE"
lastName = "JENKINS"
accountNumber = "6578147209"

driver.implicitly_wait(10)
element = driver.find_element_by_id("txtFirstName")
element.send_keys(firstName)
element = driver.find_element_by_id("txtLastName")
element.send_keys(lastName)
element = driver.find_element_by_id("txtAccountNumber")
element.send_keys(accountNumber)
driver.find_element_by_id('btnVerify1').click()

email = "divy.tolia@pseg.com"
cEmail = "divy.tolia@pseg.com"
userName="dtolia6578"
password = "test1234"
cPassword = "test1234"

driver.implicitly_wait(10)
element = driver.find_element_by_id("txtEmail")
element.send_keys(email)
element = driver.find_element_by_id("txtConfirmEmail")
element.send_keys(cEmail)
element = driver.find_element_by_id("txtUserName")
element.send_keys(userName)
element = driver.find_element_by_id("txtPassword")
element.send_keys(password)
element = driver.find_element_by_id("txtConfirmPassword")
element.send_keys(cPassword)

answer1 = "Bulls"
select_element_drp1 = Select(driver.find_element_by_id("drpSecurityQuestionOne"))
driver.implicitly_wait(10)
select_element_drp1.select_by_visible_text('High school mascot?')
element1 = driver.find_element_by_id('txtSecurityAnswer1')
element1.send_keys(answer1)