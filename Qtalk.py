
import time
#
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
#path = (r'C:\Users\veere\Desktop\Python class Assignment\test.doc')
chr=webdriver.ChromeOptions()
chr.add_experimental_option("detach",True)
lanch=webdriver.Chrome(options=chr)
lanch.get("https://chat.qspiders.com/")
lanch.find_element("xpath",'//input[@type="text"]').send_keys("9916993732")
lanch.find_element("xpath",'//input[@type="password"]').send_keys("veer3732")
lanch.find_element("xpath",'//button[@type="submit"]').click()
