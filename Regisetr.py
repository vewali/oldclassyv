import time

from selenium import webdriver
lanch = webdriver.Chrome()
lanch.get("https://demo.actitime.com/login.do")
lanch.find_element("xpath",'//input[@placeholder="Username"]').send_keys("admin")
#lanch.find_element("css selector", 'input[name="username"]').send_keys("admin")
lanch.find_element("xpath",'//input[@type="password"]').send_keys("manager")
#lanch.find_element("css selector",'input[name="pwd"]').send_keys("manager")
lanch.find_element("css selector",'input[type="checkbox"]').click()
#lanch.find_element("xpath","//div[text()='Login ']").click()
lanch.find_element("xpath","//div[text()='Login ']").click()
time.sleep(5)
lanch.close()
#chrome.find_element("css selector","input[name='register-button']").click()